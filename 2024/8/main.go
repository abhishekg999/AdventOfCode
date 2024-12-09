package main

import (
	_ "embed"
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

}

func main() {
	// part1()
	part2()
}

var nodeLocations = map[byte][][2]int{}

func part1() {
	for i := 0; i < len(lines); i++ {
		for j := 0; j < len(lines[0]); j++ {
			if lines[i][j] != '.' {
				l := nodeLocations[lines[i][j]]
				nodeLocations[lines[i][j]] = append(l, [2]int{i, j})
			}
		}
	}

	inBounds := func(i int, j int) bool {
		return i >= 0 && i < len(lines) && j >= 0 && j < len(lines[0])
	}

	unique := set{}
	for _, l := range nodeLocations {
		for i, p1 := range l {
			for j, p2 := range l {
				if i == j {
					continue
				}

				di := p2[0] - p1[0]
				dj := p2[1] - p1[1]

				if inBounds(p2[0]+di, p2[1]+dj) {
					unique[[2]int{p2[0] + di, p2[1] + dj}] = true
				}

				if inBounds(p1[0]-di, p1[1]-dj) {
					unique[[2]int{p1[0] - di, p1[1] - dj}] = true
				}
			}
		}
	}

	println(len(unique))
}

func part2() {
	for i := 0; i < len(lines); i++ {
		for j := 0; j < len(lines[0]); j++ {
			if lines[i][j] != '.' {
				l := nodeLocations[lines[i][j]]
				nodeLocations[lines[i][j]] = append(l, [2]int{i, j})
			}
		}
	}

	inBounds := func(i int, j int) bool {
		return i >= 0 && i < len(lines) && j >= 0 && j < len(lines[0])
	}

	unique := set{}
	for _, l := range nodeLocations {
		for i, p1 := range l {
			for j, p2 := range l {
				if i == j {
					continue
				}

				di := p2[0] - p1[0]
				dj := p2[1] - p1[1]

				pi := p2[0]
				pj := p2[1]
				for inBounds(pi, pj) {
					unique[[2]int{pi, pj}] = true
					pi, pj = pi+di, pj+dj
				}

				pi = p1[0]
				pj = p1[1]
				for inBounds(pi, pj) {
					unique[[2]int{pi, pj}] = true
					pi, pj = pi-di, pj-dj
				}
			}
		}
	}

	println(len(unique))

}
