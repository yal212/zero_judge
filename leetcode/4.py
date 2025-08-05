class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            big, small = nums1, nums2
        else:
            big, small = nums2, nums1
        for n in small:
            big.append(n)
        big.sort()
        l = len(big)
        if l % 2 == 0:
            median = (big[l//2]+big[l//2-1])/2
        else:
            median = big[l//2]
        return median
