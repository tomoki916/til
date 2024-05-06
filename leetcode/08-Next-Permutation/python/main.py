class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 長さが１の場合は処理する必要がない
        if len(nums) == 1:
            return

        for i in range(len(nums)-2, -1, -1):
            # nums[i+1] > nums[i]となる最大のiを求める
            if nums[i+1] > nums[i]:
                break

        # n[i]の次に大きい数を探す
        # next = 999
        # nextIndex = 0
        # for j in range(len(nums)):
        #     if nums[i] < nums[j] and nums[j] < next:
        #         nextIndex = j
        indexForSwapWith = len(nums)-1
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[i]:
                indexForSwapWith = j
                break

        # 見つからない場合は辞書順で一番最後のものなので逆順にして終わり
        if indexForSwapWith == 0:
            nums.reverse()
            return

        # n[i]をn[nextIndex]を入れ替える
        tmp = nums[i]
        nums[i] = nums[indexForSwapWith]
        nums[indexForSwapWith] = tmp

        # 新しいn[i]以降をソートする
        nums[i+1:] = sorted(nums[i+1:])
