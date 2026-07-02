class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            ci = nums[i] - 1
            if nums[i] != nums[ci]:
                nums[i], nums[ci] = nums[ci], nums[i]
            else:
                i = i+1
        for j in range(len(nums)):
            if nums[j] != j+1:
                return[nums[j],j+1]           