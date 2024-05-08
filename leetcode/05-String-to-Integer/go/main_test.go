package main

import (
	"reflect"
	"testing"
)

func TestMain(t *testing.T) {
	tests := []struct {
		name string
		s    string
		want int
	}{
		{
			"case 1",
			"42",
			42,
		},
		{
			"case 2",
			" -042",
			-42,
		},
		{
			"case 3",
			"1337c0d3",
			1337,
		},
		{
			"case 4",
			"words and 987",
			0,
		},
		{
			"case 5",
			"0-1",
			0,
		},
		{
			"case 6",
			"20000000000000000000",
			2147483647,
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			got := myAtoi(tt.s)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
