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
	part1()
	part2()
}

func part1() {

}

func part2() {
}
