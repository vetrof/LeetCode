package main

import "fmt"

func main() {
	fmt.Println(romanToInt("LVIII"))
}

func romanToInt(s string) int {
	sum := 0
	prev_value := 0

	romanianMap := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	for i := len(s) - 1; i >= 0; i-- {
		current_value := romanianMap[rune(s[i])]

		if current_value < prev_value {
			sum -= current_value
		} else {
			sum += current_value
		}

		prev_value = current_value
	}

	return sum
}
