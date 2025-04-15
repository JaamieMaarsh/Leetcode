class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < buy:
                buy = price
            else:
                max_profit += price - buy
                buy = price
        return max_profit