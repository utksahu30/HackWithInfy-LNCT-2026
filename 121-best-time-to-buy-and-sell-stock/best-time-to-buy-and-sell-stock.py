class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for current_price in prices:
            if current_price < min_price:
                min_price = current_price
            elif current_price - min_price > max_profit:
                max_profit = current_price - min_price
        return max_profit