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
			[]int{4, 5, 6, 7, 0, 1, 2},
			0,
			4,
		},
		{
			"case 2",
			[]int{4, 5, 6, 7, 0, 1, 2},
			3,
			-1,
		},

		{
			"case 3",
			[]int{1},
			0,
			-1,
		},
		{
			"case 4",
			[]int{1},
			1,
			0,
		},
		{
			"case 5",
			[]int{4, 5, 6, 7, 0, 1, 2},
			2,
			6,
		},
		{
			"case 6",
			[]int{3, 1},
			1,
			1,
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			got := search(tt.nums, tt.target)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
