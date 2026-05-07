class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numt = sorted(nums1 + nums2)
        if len(numt) % 2 != 0:
            median = numt[(len(numt)//2)]
        else:
            median = (numt[len(numt)//2]+numt[(len(numt)//2)-1]) / 2
        return median