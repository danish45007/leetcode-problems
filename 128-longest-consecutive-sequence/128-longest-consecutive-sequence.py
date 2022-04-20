class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in nums:
            # to find the start of the sequence
            # if the n-1 of n doesn't exists mean thats the start of the sequence
            if n-1 not in num_set:
                # length is the largest size of the ongoing sequence
                length = 0
                # increment the length if next subsequence of curr number exisits in set
                while n+length in num_set:
                    length +=1
                longest = max(longest,length)
        return longest
            
                    
                
            
        
        
                
