package main

import (
	"reflect"
	"testing"
)

func TestMain(t *testing.T) {
	tests := []struct {
		name string
		s    string
		want bool
	}{
		{
			"case 1",
			"()",
			true,
		},
		{
			"case 2",
			"()[]{}",
			true,
		},
		{
			"case 3",
			"(]",
			false,
		},
		{
			"case 4",
			"{[]}",
			true,
		},
		{
			"case 5",
			"]",
			false,
		},
		{
			"case 6",
			"[",
			false,
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			got := isValid(tt.s)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
