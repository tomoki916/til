package main

import (
	"reflect"
	"testing"
)

func TestMain(t *testing.T) {
	tests := []struct {
		name    string
		s       string
		numRows int
		want    string
	}{
		{
			"case 1",
			"PAYPALISHIRING",
			3,
			"PAHNAPLSIIGYIR",
		},
		{
			"case 2",
			"PAYPALISHIRING",
			4,
			"PINALSIGYAHRPI",
		},
		{
			"case 3",
			"A",
			1,
			"A",
		},
	}

	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			got := convert(tt.s, tt.numRows)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("name %v, got %v, want %v", tt.name, got, tt.want)
			}
		})
	}
}
