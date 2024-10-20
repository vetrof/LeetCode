package main

import (
	"fmt"
)

func main() {

	nums := []int{3, 3}
	target := 6

	result := twoSum(nums, target)
	fmt.Println(result)

}

func twoSum(nums []int, target int) []int {

	mapa := make(map[int]int)

	for i, num := range nums {
		diff := target - num

		if index, found := mapa[diff]; found {
			return []int{index, i}
		}

		mapa[num] = i
	}

	return nums
}
