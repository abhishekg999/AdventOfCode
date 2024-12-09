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
}

var id = []string{}

func main() {
	part1()
	part2()
}

func part1() {
	nums := intList(strings.Split(input, ""))

	tapeLength := 0
	for _, v := range nums {
		tapeLength += v
	}

	tape := make([]int, tapeLength)

	i := 0
	v := 0

	for n := 0; n < len(nums); n++ {
		for z := 0; z < nums[n]; z++ {
			if n%2 == 0 {
				tape[i] = v
			} else {
				tape[i] = -1
			}
			i++
		}
		if n%2 == 0 {
			v++
		}

	}

	l := 0
	r := len(tape) - 1

	sum := 0
	for l <= r {
		if tape[l] != -1 {
			sum += l * tape[l]
		} else {
			sum += l * tape[r]
			r--
			for tape[r] == -1 {
				r--
			}
		}
		l++
	}

	fmt.Println(sum)

}

func findEmpty(l []int, size int) int {
	i := 0
	for i+size <= len(l) {
		if l[i] == -1 {
			if slices.Equal(l[i:i+size], slices.Repeat([]int{-1}, size)) {
				return i
			}
		}
		i++
	}

	return 10e10
}

func part2() {
	nums := intList(strings.Split(input, ""))

	tapeLength := 0
	for _, v := range nums {
		tapeLength += v
	}

	tape := make([]int, tapeLength)

	i := 0
	v := 0

	for n := 0; n < len(nums); n++ {
		for z := 0; z < nums[n]; z++ {
			if n%2 == 0 {
				tape[i] = v
			} else {
				tape[i] = -1
			}
			i++
		}
		if n%2 == 0 {
			v++
		}

	}

	i = len(tape) - 1
	for i >= 0 {
		if tape[i] == -1 {
			panic("idk")
		}

		v = tape[i]

		size := 0
		for i >= 0 && tape[i] == v {
			size++
			i -= 1

		}
		i++
		start := i
		newStart := findEmpty(tape, size)

		if newStart < start {
			copy(tape[newStart:newStart+size], slices.Repeat([]int{tape[start]}, size))
			copy(tape[start:start+size], slices.Repeat([]int{-1}, size))
		}

		i -= 1
		for i >= 0 && tape[i] == -1 {
			i -= 1
		}

	}

	sum := 0
	for i, v := range tape {
		if v == -1 {
			continue
		}

		sum += i * v
	}

	println(sum)
}
