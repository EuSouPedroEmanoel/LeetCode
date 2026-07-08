package main

import (
	"fmt"
	"math"
	"strconv"
)

func reverse(x int) int {

	negativo := false

	if x < 0 {
		negativo = true
		x = -x
	}

	in_rune := []rune(strconv.Itoa(x))
	var result_rune []rune

	for i := len(in_rune) - 1; i >= 0; i-- {
		result_rune = append(result_rune, in_rune[i])
	}

	result_str := string(result_rune)
	result_int, _ := strconv.Atoi(result_str)

	if negativo {
		result_int = -result_int
	}

	if float64(result_int) < math.Pow(-2, 31) ||
		float64(result_int) > math.Pow(2, 31)-1 {
		return 0
	}

	return result_int
}

func main() {
	x := -123

	fmt.Printf("%d", reverse(x))
}
