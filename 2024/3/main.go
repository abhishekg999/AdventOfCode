package main

import (
	_ "embed"
	"fmt"
	"os"
	"regexp"
	"strconv"
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

func part1() {
	re := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	matches := re.FindAllStringSubmatch(input, -1)

	sum := 0
	for _, match := range matches {
		a := match[1]
		b := match[2]

		na, _ := strconv.Atoi(a)
		nb, _ := strconv.Atoi(b)

		sum += na * nb
	}

	fmt.Println(sum)
}

func part2() {
	re := regexp.MustCompile(`(?:mul\((\d+),(\d+)\))|(?:do\(\))|(?:don't\(\))`)
	matches := re.FindAllStringSubmatch(input, -1)

	sum := 0
	enabled := true
	for _, match := range matches {
		if match[0] == "do()" {
			enabled = true
		}

		if match[0] == "don't()" {
			enabled = false
		}

		if enabled {
			if strings.HasPrefix(match[0], "mul") {
				a := match[1]
				b := match[2]

				na, _ := strconv.Atoi(a)
				nb, _ := strconv.Atoi(b)

				sum += na * nb
			}
		}
	}

	fmt.Println(sum)

}

func main() {
	// part1()
	part2()
}
