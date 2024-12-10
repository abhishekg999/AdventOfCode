package main

import (
	_ "embed"
	"fmt"
	"slices"
	. "strconv"
	"strings"
)

func fatal(err error) {
	if err != nil {
		panic(err)
	}
}

func must[T any](value T, err error) T {
	fatal(err)
	return value
}

//go:embed input
var input string
var lines []string

type set map[any]bool

func intList(inp []string) []int {
	ret := []int{}
	for _, val := range inp {
		ret = append(ret, must(Atoi(val)))
	}
	return ret
}

func init() {
	input = strings.TrimRight(input, "\n")

	if len(input) == 0 {
		panic("empty input")
	}

	lines = strings.Split(input, "\n")

	for _, line := range lines {
		grid = append(grid, []byte(line))
	}
}

func main() {
	part1()
	part2()
}

var grid [][]byte

func part1() {
	starts := [][2]int{}
	for i, line := range grid {
		for j, val := range line {
			if val == '0' {
				starts = append(starts, [2]int{i, j})
			}
		}
	}

	cache := [][]int{}
	for i := 0; i < len(grid); i++ {
		cache = append(cache, slices.Repeat([]int{-1}, len(grid[i])))
	}

	sum := 0

	for _, t := range starts {
		seen := set{}
		sum += traverse(seen, t[0], t[1])
	}

	fmt.Println(sum)

}

var directions = [][2]int{
	{0, 1},
	{0, -1},
	{1, 0},
	{-1, 0},
}

func traverse(seen set, i int, j int) int {
	if grid[i][j] == '9' && !seen[[2]int{i, j}] {
		seen[[2]int{i, j}] = true
		return 1
	}
	tot := 0
	for _, t := range directions {
		ni := i + t[0]
		nj := j + t[1]

		if 0 <= ni && ni < len(grid) && 0 <= nj && nj < len(grid[i]) && grid[i][j]+1 == grid[ni][nj] {
			tot += traverse(seen, ni, nj)
		}
	}

	return tot
}

func val(cache [][]int, i int, j int) int {
	if grid[i][j] == '9' {
		cache[i][j] = 1
	} else if cache[i][j] == -1 {
		cache[i][j] = 0
		for _, t := range directions {
			ni := i + t[0]
			nj := j + t[1]

			if 0 <= ni && ni < len(grid) && 0 <= nj && nj < len(grid[i]) && grid[i][j]+1 == grid[ni][nj] {
				cache[i][j] += val(cache, ni, nj)
			}
		}
	}
	return cache[i][j]
}

func part2() {
	starts := [][2]int{}
	for i, line := range grid {
		for j, val := range line {
			if val == '0' {
				starts = append(starts, [2]int{i, j})
			}
		}
	}

	cache := [][]int{}
	for i := 0; i < len(grid); i++ {
		cache = append(cache, slices.Repeat([]int{-1}, len(grid[i])))
	}

	sum := 0
	for _, t := range starts {
		sum += val(cache, t[0], t[1])
	}

	fmt.Println(sum)

}
