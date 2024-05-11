package main

import (
	"reflect"
	"testing"
)

func TestMain(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		target int
		want   int
	}{
		{
			"case 1",
			[]int{1, 3, 5, 6},
			5,
			2,
		},
		{
			"case 2",
			[]int{1, 3, 5, 6},
			2,
			1,
		},
		{
			"case 3",
			[]int{1, 3, 5, 6},
			7,
			4,
		},
		{
			"case 4",
			[]int{0},
			1,
			1,
		},
		{
			"case 5",
			[]int{1, 3, 5, 6},
			0,
			0,
		},
		{
			"case 6",
			[]int{1, 3, 5, 6},
			1,
			0,
		},
		{
			"case 7",
			[]int{1, 3, 5, 6},
			2,
			1,
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			got := searchInsert(tt.nums, tt.target)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
