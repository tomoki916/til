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
			"abcabcbb",
			3,
		},
		{
			"case 2",
			"bbbbb",
			1,
		},
		{
			"case 3",
			"pwwkew",
			3,
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			got := lengthOfLongestSubstring(tt.s)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
