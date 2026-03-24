class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = prices[0]
        prof = 0
        for i in prices:
            if i < mini:
                prof = max(maxi - mini , prof)
                mini = i
                maxi = i
            elif i > maxi:
                maxi = i
        return(max(maxi-mini,prof))