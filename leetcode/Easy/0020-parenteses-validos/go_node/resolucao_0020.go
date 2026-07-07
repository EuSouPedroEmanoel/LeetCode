package main

import "C"

// export isValid
func isValid(s string) bool {
	mapeamento := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	stack := []rune{}

	for _, char := range s {
		aberturaEsperada, ok := mapeamento[char]

		if ok {
			if len(stack) == 0 {
				return false
			}

			topo := stack[len(stack)-1]
			// Remove o elemento do topo (Pop)
			stack = stack[:len(stack)-1]

			if topo != aberturaEsperada {
				return false
			}
		} else {
			stack = append(stack, char)
		}
	}

	return len(stack) == 0
}

func main() {}
