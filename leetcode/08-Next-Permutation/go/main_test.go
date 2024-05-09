package main

import (
	"reflect"
	"testing"
)

func TestMain(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			"case 1",
			[]int{1, 2, 3},
			[]int{1, 3, 2},
		},
		{
			"case 2",
			[]int{3, 2, 1},
			[]int{1, 2, 3},
		},

		{
			"case 3",
			[]int{1, 1, 5},
			[]int{1, 5, 1},
		},
		{
			"case 4",
			[]int{1, 3, 2},
			[]int{2, 1, 3},
		},
		{
			"case 5",
			[]int{2, 1, 3},
			[]int{2, 3, 1},
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			nextPermutation(tt.nums)
			got := tt.nums
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
