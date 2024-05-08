package main

import (
	"reflect"
	"testing"
)

func TestMain(t *testing.T) {
	tests := []struct {
		name string
		n    int
		want []string
	}{
		{
			"case 1",
			3,
			[]string{"((()))", "(()())", "(())()", "()(())", "()()()"},
		},
		{
			"case 2",
			1,
			[]string{"()"},
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			got := generateParenthesis(tt.n)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
