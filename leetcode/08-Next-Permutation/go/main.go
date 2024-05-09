package main

import (
	"fmt"
	"sort"
)

func nextPermutation(nums []int) {
	// nums[i] < nums[i+1]となる最大のiを見つける
	indexForSwap := -1
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			indexForSwap = i
			break
		}
	}
	fmt.Printf("indexForSwap: %v\n", indexForSwap)
	if indexForSwap == -1 {
		// 逆順に並んでいるのでソートして完了
		sort.Ints(nums)
		return
	}

	// nums[i]の次の大きいnums[j]を見つける
	indexSwapWith := 0
	tmpMax := 999
	for j := indexForSwap; j < len(nums); j++ {
		if nums[indexForSwap] < nums[j] && nums[j] < tmpMax {
			tmpMax = nums[j]
			indexSwapWith = j
		}
	}
	fmt.Printf("indexSwapWith: %v\n", indexSwapWith)

	// nums[i]とnums[j]を入れ替える
	nums[indexForSwap], nums[indexSwapWith] = nums[indexSwapWith], nums[indexForSwap]

	// 入れ替え後、nums[i]以降をソートする
	sort.Ints(nums[indexForSwap+1:])
}
