package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(isPalindrome(122231))
}

func isPalindrome(x int) bool {

	strInt := strconv.Itoa(x)
	leght := len(strInt) - 1

	for i := 0; i < len(strInt); i++ {

		a, _ := strconv.Atoi(string(strInt[i]))
		b, _ := strconv.Atoi(string(strInt[leght-i]))

		if a != b {
			return false
		}
	}

	return true

}
