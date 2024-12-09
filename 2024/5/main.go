package main

import (
	_ "embed"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func fatal(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}

func mustValue(value interface{}, err error) interface{} {
	if err != nil {
		panic(err)
	}
	return value
}

//go:embed input
var input string
var lines []string
var g = make(map[int][]int)

var updates = [][]int{}

func init() {
	input = strings.TrimRight(input, "\n")

	if len(input) == 0 {
		panic("empty input")
	}

	lines = strings.Split(input, "\n")

	var i int = 0
	for i = 0; i < len(lines); i++ {
		line := lines[i]
		if len(line) == 0 {
			break
		}

		prev, next := strings.Split(line, "|")[0], strings.Split(line, "|")[1]
		g[mustValue(strconv.Atoi(prev)).(int)] = append(g[mustValue(strconv.Atoi(prev)).(int)], mustValue(strconv.Atoi(next)).(int))
	}

	for i = i + 1; i < len(lines); i++ {
		line := lines[i]

		if len(strings.Split(line, ","))%2 == 0 {
			panic("invalid update")
		}

		nums := []int{}
		for _, s := range strings.Split(line, ",") {
			nums = append(nums, mustValue(strconv.Atoi(s)).(int))
		}
		updates = append(updates, nums)
	}

}

func main() {
	part1()
	part2()
}

func validate(update []int) bool {
	for key, value := range g {
		i := slices.Index(update, key)
		if i != -1 {
			for _, v := range value {
				if slices.Index(update[:i], v) != -1 {
					return false
				}
			}
		}
	}

	return true
}

func isolateRules(update []int) map[int][]int {
	usefulRules := map[int][]int{}
	for key, value := range g {
		i := slices.Index(update, key)
		if i != -1 {
			for _, v := range value {
				if slices.Index(update, v) != -1 {
					usefulRules[key] = append(usefulRules[key], v)
				}
			}
		}
	}

	return usefulRules
}

func part1() {
	sum := 0
	for _, update := range updates {
		if validate(update) {
			mid := len(update) / 2
			sum += update[mid]
		}
	}

	fmt.Println(sum)
}

func part2() {
	sum := 0
	for _, update := range updates {
		if !validate(update) {
			rules := isolateRules(update)
			fmt.Println(update)
			fmt.Println(rules)

			slices.SortFunc(update, func(a, b int) int {
				return len(rules[b]) - len(rules[a])
			})

			mid := len(update) / 2
			sum += update[mid]
		}
	}

	fmt.Println(sum)

}
