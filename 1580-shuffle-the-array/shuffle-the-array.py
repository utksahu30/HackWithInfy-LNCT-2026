class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        num1 = nums[0:n//2]
        num2 = nums[n//2:n]
        i = 0
        temp = []
        for i in range(0,n//2):
            temp.append(num1[i])
            temp.append(num2[i])
            
        return temp