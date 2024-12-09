package main

import (
	_ "embed"
	"fmt"
	"os"
	"strings"
)

func fatal(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

//go:embed input
var input string

func init() {
	input = strings.TrimRight(input, "\n")

	if len(input) == 0 {
		panic("empty input")
	}

}

var directions = [][]int{
	{1, 0},
	{0, 1},
	{-1, 0},
	{0, -1},
	{1, 1},
	{-1, -1},
	{1, -1},
	{-1, 1},
}

func part1() {
	lines := strings.Split(input, "\n")
	grid := make([][]byte, len(lines))

	for i, line := range lines {
		grid[i] = []byte(line)
	}

	count := 0
	to_find := "XMAS"

	for y := 0; y < len(grid); y++ {
		for x := 0; x < len(grid[y]); x++ {
			for _, dir := range directions {
				new_x := x
				new_y := y

				found := true
				for i := 0; i < len(to_find); i++ {
					if new_x < 0 || new_x >= len(grid[y]) || new_y < 0 || new_y >= len(grid) {
						found = false
						break
					}

					if grid[new_y][new_x] != to_find[i] {
						found = false
						break
					}

					new_x += dir[0]
					new_y += dir[1]
				}

				if found {
					count++
				}

			}
		}
	}

	fmt.Println(count)

}

var diagonal = [][]int{
	{1, 1},
	{1, -1},
}

func part2() {
	lines := strings.Split(input, "\n")
	grid := make([][]byte, len(lines))

	for i, line := range lines {
		grid[i] = []byte(line)
	}

	count := 0

	for y := 1; y < len(grid)-1; y++ {
		for x := 1; x < len(grid[y])-1; x++ {
			if grid[y][x] != 'A' {
				continue
			}

			valid := true
			for _, dir := range diagonal {
				forward_y := y + dir[0]
				forward_x := x + dir[1]

				backward_y := y - dir[0]
				backward_x := x - dir[1]

				fmt.Println(forward_y, forward_x, backward_y, backward_x, string(grid[forward_y][forward_x]), string(grid[backward_y][backward_x]))

				if !((grid[forward_y][forward_x] == 'M' && grid[backward_y][backward_x] == 'S') ||
					(grid[forward_y][forward_x] == 'S' && grid[backward_y][backward_x] == 'M')) {
					valid = false
					break
				}
			}

			if valid {
				fmt.Println("3x3 diagonal grid around", x, y)
				for dy := -1; dy <= 1; dy++ {
					for dx := -1; dx <= 1; dx++ {
						fmt.Print(string(grid[y+dy][x+dx]), " ")
					}
					fmt.Println()
				}
				count++
			}

		}
	}

	fmt.Println(count)
}

func main() {
	// part1()
	part2()
}
