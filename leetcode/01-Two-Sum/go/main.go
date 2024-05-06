package main

func twoSum(nums []int, target int) []int {
	var result []int
	cache := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		_, isCached := cache[nums[i]]
		if isCached {
			result = append(result, cache[nums[i]])
			result = append(result, i)
			break
		}

		diff := target - nums[i]
		cache[diff] = i
	}
	return result
}
