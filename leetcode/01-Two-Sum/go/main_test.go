package main

import (
	"reflect"
	"testing"
)

func TestMain(t *testing.T) {
	// t.Parallel()
	tests := []struct {
		name   string
		nums   []int
		target int
		want   []int
	}{
		{
			"case 1",
			[]int{2, 7, 11, 15},
			9,
			[]int{0, 1},
		},
		{
			"case 2",
			[]int{3, 2, 4},
			6,
			[]int{1, 2},
		},
		{
			"case 3",
			[]int{3, 3},
			6,
			[]int{0, 1},
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			// t.Parallel()
			got := twoSum(tt.nums, tt.target)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
