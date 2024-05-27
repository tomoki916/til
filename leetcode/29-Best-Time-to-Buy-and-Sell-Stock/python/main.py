class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            maxProfit = max(currentProfit, maxProfit)

            # マイナスになったらそこがbuy priceとしてそこまでの範囲で最小
            if currentProfit < 0:
                left = right
            right += 1

        return maxProfit
