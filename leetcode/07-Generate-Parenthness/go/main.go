package main

import "slices"

func generateParenthesis(n int) []string {
	result := make([]string, 0)

	genetate(n, 0, 0, "", &result)

	return result
}

func genetate(n int, left int, right int, s string, result *[]string) {
	if len(s) == 2*n && !slices.Contains(*result, s) {
		*result = append(*result, s)
		return
	}

	if left > right {
		genetate(n, left, right+1, s+")", result)
	}
	if left < n {
		genetate(n, left+1, right, s+"(", result)
	}
}
