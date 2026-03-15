class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        y = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                x = x+1
                y = max(x,y)
            else:
                x = 0
        return y