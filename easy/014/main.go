package main

import "fmt"

func main() {

	s := []string{"flower", "flow", "flight"}

	fmt.Println(longestCommonPrefix(s))

}

func longestCommonPrefix(strs []string) string {
	prefix := ""
	temp := strs[0]
	for _, word := range strs[1:] {

		for i, _ := range word {

			fmt.Println(string(word[i]), string(temp[i]))

			if temp[i] == word[i] {
				prefix += string(word[i])
			} else {
				return prefix
			}

		}
	}

	return prefix

}
