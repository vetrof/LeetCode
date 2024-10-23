package main

import "fmt"

func main() {

	//s := []string{"flower", "flow", "flight"}
	//s := []string{"dog", "racecar", "car"}
	s := []string{"ab", "a"}

	fmt.Println(longestCommonPrefix(s))

}

func longestCommonPrefix(strs []string) string {
	prefix := ""

	for indexFirstChar, charFirstWord := range strs[0] {
		for _, word := range strs[1:] {

			if indexFirstChar > len(word)-1 {
				return prefix
			}

			if charFirstWord != rune(word[indexFirstChar]) {
				return prefix
			}
		}

		prefix += string(charFirstWord)

	}
	return prefix
}
