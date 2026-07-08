package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	for i := range strs[0] {
		for j := range strs {
			if i == len(strs[j]) ||
				strs[j][i] != strs[0][i] {
				return strs[0][:i]
			}
		}
	}
	return strs[0]
}

func main() {
	frases := []string{
		"carro", "carroça", "carta",
	}

	fmt.Println(longestCommonPrefix(frases))
}
