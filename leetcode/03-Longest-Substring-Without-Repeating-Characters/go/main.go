package main

func lengthOfLongestSubstring(s string) int {
	left := 0
	result := 0
	cache := make(map[string]int)

	for right := 0; right < len(s); right++ {
		currentChar := s[right : right+1]
		if cachedIndex, hasCache := cache[currentChar]; hasCache && cachedIndex >= left {
			left = cachedIndex + 1
		}

		cache[currentChar] = right
		currentLength := right - left + 1
		if currentLength > result {
			result = currentLength
		}
	}

	return result
}
