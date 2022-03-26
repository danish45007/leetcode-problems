class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set = set()
        intersection_set = set()
        for num in nums1:
            num_set.add(num)
        
        for num in nums2:
            if(num in num_set):
                intersection_set.add(num)
        
        return list(intersection_set)
            