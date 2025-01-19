class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using 2 pointer method
        l = 0 #index
        r = l+1
        max_profit = 0

        while r<len(prices):
            if prices[r]>prices[l]:
                profit = prices[r]-prices[l]
                max_profit = max(max_profit, profit)
            else:
                l=r
            r+=1
        return max_profit