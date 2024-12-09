package main

import (
	_ "embed"
	"fmt"
	"math"
	"os"
	"sort"
	"strings"
)

func fatal(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

//go:embed input
var data string

func init() {
}

func part1() {
	lines := strings.Split(string(data), "\n")

	var l []int
	var r []int
	for _, line := range lines {
		if line == "" {
			continue
		}
		var num1, num2 int
		_, err := fmt.Sscanf(line, "%d   %d", &num1, &num2)
		fatal(err)
		l = append(l, num1)
		r = append(r, num2)
	}

	sort.Ints(l)
	sort.Ints(r)

	sum := 0
	for i := 0; i < len(l); i++ {
		sum += int(math.Abs(float64(r[i] - l[i])))
	}

	fmt.Println(sum)
}

func part2() {
	lines := strings.Split(string(data), "\n")

	var l []int
	var r []int
	for _, line := range lines {
		if line == "" {
			continue
		}
		var num1, num2 int
		_, err := fmt.Sscanf(line, "%d   %d", &num1, &num2)
		fatal(err)
		l = append(l, num1)
		r = append(r, num2)
	}

	sort.Ints(r)
	rFreq := make(map[int]int)
	for _, v := range r {
		rFreq[v]++
	}

	sum := 0
	for _, v := range l {
		sum += v * rFreq[v]
	}

	fmt.Println(sum)

}

func main() {
	// part1()
	part2()
}
