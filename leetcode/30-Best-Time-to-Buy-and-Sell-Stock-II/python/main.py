class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # result = 0
        # for i in range(1, len(prices)):
        #     currentPrice = prices[i-1]
        #     if currentPrice < prices[i]:
        #         result += prices[i] - currentPrice
        # return result

        n = len(prices)
        opt = [0] * n
        opt[0] = 0

        # for i in range(1, n):
        #     opt[i] = max(opt[i-1], opt[i-1] + (prices[i]-prices[i-1]))

        # return opt[-1]
        for i in range(1, n):
            opt[i] = max(0, (prices[i]-prices[i-1]))

        return sum(opt)
