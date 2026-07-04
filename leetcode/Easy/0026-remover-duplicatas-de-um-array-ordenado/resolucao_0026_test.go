package main

import (
	"reflect"
	"testing"
)

func TestRemoveDuplicates(t *testing.T) {
	tests := []struct {
		name         string
		nums         []int
		expectedK    int
		expectedNums []int
	}{
		{
			name:         "Caso básico",
			nums:         []int{1, 1, 2},
			expectedK:    2,
			expectedNums: []int{1, 2},
		},
		{
			name:         "Caso com mais duplicatas",
			nums:         []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
			expectedK:    5,
			expectedNums: []int{0, 1, 2, 3, 4},
		},
		{
			name:         "Slice vazio",
			nums:         []int{},
			expectedK:    0,
			expectedNums: []int{},
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			numsCopia := make([]int, len(tc.nums))
			copy(numsCopia, tc.nums)

			actualK := removeDuplicates(numsCopia)

			if actualK != tc.expectedK {
				t.Errorf("Esperava k = %d, mas veio %d", tc.expectedK, actualK)
			}

			var actualNums []int
			if actualK > 0 {
				actualNums = numsCopia[:actualK]
			} else {
				actualNums = []int{}
			}

			if !reflect.DeepEqual(actualNums, tc.expectedNums) {
				t.Errorf("Esperava o slice %v, mas veio %v", tc.expectedNums, actualNums)
			}
		})
	}
}
