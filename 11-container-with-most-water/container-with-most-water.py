class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force 
        '''maxw = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1,n):
                h = min(height[i],height[j])
                w = j - i
                maxwn = h*w
                maxw = max(maxw,maxwn)
        return maxw'''
        maxw = 0
        l,r = 0, len(height)-1
        while l < r:
            h = min(height[l],height[r])
            w = r - l
            maxwn = h*w
            maxw = max(maxw,maxwn)
        
            if height[l]<height[r]:
                l = l+1
            else:
                r = r-1
        return maxw