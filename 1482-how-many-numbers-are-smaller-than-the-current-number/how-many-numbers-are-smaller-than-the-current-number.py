class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sn = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(0,len(nums)):
                if j == i:
                    continue
                if nums[j] < nums[i]:
                    sn[i] = sn[i] + 1
        return sn