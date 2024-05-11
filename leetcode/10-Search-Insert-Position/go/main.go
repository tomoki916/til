package main

import "fmt"

func searchInsert(nums []int, target int) int {
	left, right := 0, len(nums)-1
	var mid int
	result := -1

	fmt.Println()
	for left <= right {
		mid = (left + right) / 2 // int型なので切り捨て
		fmt.Printf("Start left: %v, mid: %v, right: %v\n", left, mid, right)

		if nums[mid] == target {
			result = mid
			break
		}

		if target < nums[left] {
			// 今のグループの左側にある
			result = left
			break
		} else if nums[right] < target {
			// 今のグループの右側にある
			result = right + 1
			break
		}

		if nums[left] <= target && target < nums[mid] {
			// 左側のグループにある
			right = mid - 1
		} else {
			// 右側のグループにある
			left = mid + 1
		}
		fmt.Printf("End left: %v, mid: %v, right: %v\n", left, mid, right)

	}

	return result
}
