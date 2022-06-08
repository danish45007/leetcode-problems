class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        '''
            Time:O(n*k)
            Space:O(2^k)
        '''
        unique_code_set = set()
        l,r = 0,0
        while r < len(s):
            if r-l+1 == k:
                unique_code_set.add(s[l:r+1])
                l+=1
            r +=1
        return len(unique_code_set) == 2**k
        
        # optimization using rolling hash
        '''
            Time: O(n)
            Space: O(2^k)
        '''
        # N = 2**k
        # found = [False]*N
        # all_one = N-1
        # hash_val = 0
        # for i in range(len(s)):
        #     hash_val = ((hash_val << 1) and all_one) or (ord(s[i]) - ord('0'))
        #     if i >= k-1 and not found[hash_val]:
        #         found[hash_val] = True
        #         N -= 1
        #     if N == 0: return True
        # return False
                