class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1,s2 = [],[]
        s1.append(list(set(nums1)-set(nums2)))
        s2.append(list(set(nums2)-set(nums1)))
        return [s1[0],s2[0]]