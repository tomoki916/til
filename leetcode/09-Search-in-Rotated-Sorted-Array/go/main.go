package main

import "fmt"

func search(nums []int, target int) int {
	left, right := 0, len(nums)-1

	result := -1

	fmt.Println()
	for left <= right {
		mid := (left + right) / 2 // int型なので切り捨て
		fmt.Printf("Start left: %v, mid: %v, right: %v\n", left, mid, right)

		if nums[mid] == target {
			result = mid
			break
		}

		if nums[left] <= nums[mid] {
			// 境界が右側にある場合
			if nums[left] <= target && target < nums[mid] {
				// 左側に存在するので次のループは左側
				right = mid - 1
			} else {
				// 右側に存在するので次のループは右側
				left = mid + 1
			}
		} else {
			// 境界が左側にある場合
			if nums[mid] < target && target <= nums[right] {
				// 右側に存在するので次のループは右側
				left = mid + 1
			} else {
				// 左側に存在するので次のループは左側
				right = mid - 1
			}
		}
		fmt.Printf("End left: %v, mid: %v, right: %v\n", left, mid, right)

	}

	return result
}
