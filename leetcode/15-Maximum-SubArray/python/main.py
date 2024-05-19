class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximamSum = -(10**4)
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum > maximamSum:
                maximamSum = currentSum

            if currentSum < 0:
                # 合計が負の値になった場合、次の数を足した合計値よりも次の数単体の方が大きくなる。
                # そのため、合計値が負になった時点で合計値をリセットする
                currentSum = 0

        return maximamSum
