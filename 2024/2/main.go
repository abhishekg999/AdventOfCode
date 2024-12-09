package main

import (
	_ "embed"
	"fmt"
	"math"
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

func Safe(l []int) bool {
	if l[0] == l[1] {
		return false
	}

	increasing := true
	decreasing := true

	for i := 1; i < len(l); i++ {
		if l[i] <= l[i-1] {
			increasing = false
		}
		if l[i] >= l[i-1] {
			decreasing = false
		}

		if math.Abs(float64(l[i]-l[i-1])) < 1 || math.Abs(float64(l[i]-l[i-1])) > 3 {
			return false
		}
	}

	if !increasing && !decreasing {
		return false
	}

	return true
}

func SafeLoose(l []int) bool {
	newList := make([]int, len(l)-1)
	for i := 0; i < len(l); i++ {
		copy(newList[:i], l[:i])
		copy(newList[i:], l[i+1:])

		if Safe(newList) {
			return true
		}
	}
	return false
}

func part1() {
	lines := strings.Split(input, "\n")
	formattedInput := make([][]int, len(lines))

	for i, line := range lines {
		numStrs := strings.Fields(line)
		formattedInput[i] = make([]int, len(numStrs))
		for j, numStr := range numStrs {
			var num int
			_, err := fmt.Sscanf(numStr, "%d", &num)
			fatal(err)
			formattedInput[i][j] = num
		}
	}

	safe := 0
	for _, l := range formattedInput {
		if Safe(l) {
			safe++
			fmt.Println(l)
		}
	}

	fmt.Println(safe)
}

func part2() {
	lines := strings.Split(input, "\n")
	formattedInput := make([][]int, len(lines))

	for i, line := range lines {
		numStrs := strings.Fields(line)
		formattedInput[i] = make([]int, len(numStrs))
		for j, numStr := range numStrs {
			var num int
			_, err := fmt.Sscanf(numStr, "%d", &num)
			fatal(err)
			formattedInput[i][j] = num
		}
	}

	safe := 0
	for _, l := range formattedInput {
		if SafeLoose(l) {
			safe++
		}
	}

	fmt.Println(safe)

}

func main() {
	part2()
}
