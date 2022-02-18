class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for ele in nums:
            try:
                dict[ele] += 1
            except:
                dict[ele] = 1

        for item in dict:

             # if frequency is more than 1
             # print the element
            if(dict[item] > 1):
                return item
