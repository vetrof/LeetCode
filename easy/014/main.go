package main

import "fmt"

func main() {

	s := []string{"flower", "flow", "flight"}

	fmt.Println(longestCommonPrefix(s))

}

func longestCommonPrefix(strs []string) string {

	fmt.Println(strs)

	return strs[0]

}
