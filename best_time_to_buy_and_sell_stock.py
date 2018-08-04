#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        if n > 0:
            i = 1
            buy_price = prices[0]
            while i < n:
                if buy_price > prices[i]:
                    buy_price = prices[i]
                else:
                    profit = max(prices[i] - buy_price, profit)
                i = i + 1

        return profit
