class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        
        for p in prices:
            if p < buy1:
                buy1 = p
            if p - buy1 > sell1:
                sell1 = p - buy1
            if p - sell1 < buy2:
                buy2 = p - sell1
            if p - buy2 > sell2:
                sell2 = p - buy2
        return sell2