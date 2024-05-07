package main

import (
	"strings"
)

func convert(s string, numRows int) string {
	if len(s) == 1 || numRows == 1 {
		return s
	}

	table := make([][]string, numRows)
	currentRow := 0
	goDown := true

	for i := 0; i < len(s); i++ {
		currentChar := s[i : i+1]
		table[currentRow] = append(table[currentRow], currentChar)

		if currentRow == 0 {
			goDown = true
		} else if currentRow == numRows-1 {
			goDown = false
		}

		if goDown {
			currentRow += 1
		} else {
			currentRow -= 1
		}
	}

	tmpList := []string{}
	for i := 0; i < len(table); i++ {
		tmpList = append(tmpList, strings.Join(table[i], ""))
	}

	return strings.Join(tmpList, "")

}
