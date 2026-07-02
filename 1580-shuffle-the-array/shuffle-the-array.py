class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #n = len(nums)
        #n already defined and if n is even, no need to use //2 all the time
        num1 = nums[0:n]
        num2 = nums[n:]
        #i = 0
        temp = []
        for i in range(0,n):
            temp.append(num1[i])
            temp.append(num2[i])
            
        return temp