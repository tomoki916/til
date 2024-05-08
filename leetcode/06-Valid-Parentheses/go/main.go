package main

func isValid(s string) bool {
	var stack []rune
	result := true

	for _, char := range s {
		if char == '(' || char == '[' || char == '{' {
			stack = append(stack, char)
		} else if len(stack) > 0 && stack[len(stack)-1] == '(' && char == ')' {
			stack = stack[:len(stack)-1]
		} else if len(stack) > 0 && stack[len(stack)-1] == '{' && char == '}' {
			stack = stack[:len(stack)-1]
		} else if len(stack) > 0 && stack[len(stack)-1] == '[' && char == ']' {
			stack = stack[:len(stack)-1]
		} else {
			result = false
			break
		}
	}

	if len(stack) > 0 {
		result = false
	}
	return result
}
