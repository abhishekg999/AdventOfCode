package main

import (
	_ "embed"
	"strconv"
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
		ret = append(ret, must(strconv.Atoi(val)))
	}
	return ret
}

func init() {
	input = strings.TrimRight(input, "\n")

	if len(input) == 0 {
		panic("empty input")
	}

	lines = strings.Split(input, "\n")
}

func main() {
	// part1()
	part2()
}

var si, sj int
var dir int

var directions = [][]int{
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1},
}

func part1() {
	grid := [][]rune{}
	for i, line := range lines {
		grid = append(grid, []rune(line))

		for j, c := range line {

			switch c {
			case '^':
				si, sj = i, j
				dir = 0
			case '>':
				si, sj = i, j
				dir = 1
			case 'v':
				si, sj = i, j
				dir = 2
			case '<':
				si, sj = i, j
				dir = 3
			}
		}
	}

	for si >= 0 && si < len(grid) && sj >= 0 && sj < len(grid[0]) {
		grid[si][sj] = 'X'

		ni, nj := si+directions[dir][0], sj+directions[dir][1]
		if ni < 0 || ni >= len(grid) || nj < 0 || nj >= len(grid[0]) {
			break
		}

		if grid[ni][nj] != '#' {
			si, sj = ni, nj
		} else {
			dir = (dir + 1) % 4
		}
	}

	sum := 0
	for _, line := range grid {
		for _, c := range line {
			if c == 'X' {
				sum++
			}
		}
	}

	println(sum)

}

func path(grid [][]rune, si, sj, dir int, cgraph map[[3]int]bool) bool {
	for si >= 0 && si < len(grid) && sj >= 0 && sj < len(grid[0]) {
		if cgraph[[3]int{si, sj, dir}] {
			return false
		}
		cgraph[[3]int{si, sj, dir}] = true

		ni, nj := si+directions[dir][0], sj+directions[dir][1]

		if ni < 0 || ni >= len(grid) || nj < 0 || nj >= len(grid[0]) {
			break
		}

		if grid[ni][nj] != '#' {
			si, sj = ni, nj
		} else {
			dir = (dir + 1) % 4
		}
	}

	return true
}

func part2() {
	grid := [][]rune{}
	for i, line := range lines {
		grid = append(grid, []rune(line))

		for j, c := range line {

			switch c {
			case '^':
				si, sj = i, j
				dir = 0
			case '>':
				si, sj = i, j
				dir = 1
			case 'v':
				si, sj = i, j
				dir = 2
			case '<':
				si, sj = i, j
				dir = 3
			}
		}
	}

	sum := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] != '.' {
				continue
			}

			cgraph := map[[3]int]bool{}
			grid[i][j] = '#'

			if !path(grid, si, sj, dir, cgraph) {
				sum += 1
			}

			grid[i][j] = '.'
		}
	}

	println(sum)

}
