class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        u = 0
        for i in range(0,len(nums),2):
            u = u + nums[i]
        return u
        