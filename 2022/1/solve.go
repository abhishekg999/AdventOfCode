package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func Map[T, U any](s []T, f func(T) U) []U {
	r := make([]U, len(s))
	for i, v := range s {
		r[i] = f(v)
	}
	return r
}

func Sum(arr []int) int {
	ret := 0
	for _, v := range arr {
		ret += v
	}

	return ret
}

func main() {
	_input, _ := os.ReadFile("input")
	input := string(_input)

	max := 0
	for _, j := range strings.Split(input, "\n\n") {
		cur := strings.Split(j, "\n")
		l := Map(cur, func(x string) int {
			val, _ := strconv.Atoi(x)
			return val
		})

		sum := Sum(l)
		if sum > max {
			max = sum
		}
	}

	fmt.Println(max)
}
