package main

import (
	_ "embed"
	"fmt"
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

func concat(a int, b int) int {
	return must(Atoi(Itoa(a) + Itoa(b)))
}

func test(target int, cur int, rem []int) bool {
	if cur > target {
		return false
	}

	if cur == target && len(rem) == 0 {
		return true
	}

	if len(rem) == 0 {
		return false
	}
	return test(target, cur+rem[0], rem[1:]) ||
		test(target, cur*rem[0], rem[1:]) ||
		test(target, concat(cur, rem[0]), rem[1:])

}

func part1() {
	sum := 0

	for _, line := range lines {
		i := strings.Index(line, ":")
		target := must(Atoi(line[:i]))
		vals := intList(strings.Fields(line[i+1:]))

		if test(target, 0, vals) {
			sum += target
		}
	}
	fmt.Println(sum)

}

func part2() {
}
