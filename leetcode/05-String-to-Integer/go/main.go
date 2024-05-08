package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
	"unicode"
)

func _myAtoi(s string) int {
	sign := 1
	res := 0

	s = strings.TrimLeft(s, " ")

	if len(s) == 0 {
		return res
	}

	if s[0] == '-' {
		sign = -1
		s = s[1:]
	} else if s[0] == '+' {
		s = s[1:]
	}

	for _, ch := range s {
		if !unicode.IsDigit(ch) {
			break
		}

		dig := int(ch - '0')
		res = res*10 + dig

		if sign*res < math.MinInt32 {
			return math.MinInt32
		} else if sign*res > math.MaxInt32 {
			return math.MaxInt32
		}
	}

	return sign * res
}

func myAtoi(s string) int {
	result := 0
	numString := ""

	isLeadingWhitespace := true
	signChar := ""

	numMap := make(map[string]int)
	for i := 0; i < 10; i++ {
		numMap[strconv.Itoa(i)] = i
	}

	for i := 0; i < len(s); i++ {
		currentChar := s[i : i+1]

		// 先頭のスペースは読み飛ばす
		if isLeadingWhitespace && currentChar == " " {
			continue
		}
		if currentChar != " " {
			isLeadingWhitespace = false
		}

		// 符号が出てきたら格納する
		if numString == "" && signChar == "" && currentChar == "-" {
			signChar = "-"
			continue
		}
		if numString == "" && signChar == "" && currentChar == "+" {
			signChar = "+"
			continue
		}

		// 数字以外が出てきたらループを抜ける
		if _, isNum := numMap[currentChar]; !isNum {
			break
		}

		// 数字であればそれを控える
		numString += currentChar
	}
	fmt.Printf("numString: %v\n", numString)

	// 数字に変換する
	var tmp float64
	for i := 0; i < len(numString); i++ {
		tmp += float64(numMap[numString[i:i+1]]) * math.Pow10(len(numString)-i-1)
	}
	fmt.Printf("tmp: %v\n", tmp)

	// 符号を適用する
	if signChar == "-" {
		tmp = tmp * -1
	}

	// 範囲を確認する
	if tmp < math.Pow(-2, 31) {
		result = int(math.Pow(-2, 31))
	} else if tmp > math.Pow(2, 31)-1 {
		result = int(math.Pow(2, 31)) - 1
	} else {
		result = int(tmp)
	}
	fmt.Printf("result: %v\n", result)

	return result
}
