class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # Time: O(nk) where n,k is size of s and size of removable
        # Space: O(k)
        
        # removed = set()
        # def is_subsequence(_s,_p):
        #     i,j = 0,0
        #     while i < len(_s) and j < len(_p):
        #         if _s[i] != _p[j] or i in removed:
        #             i +=1
        #             continue
        #         # matched
        #         i +=1
        #         j +=1
        #     return j == len(_p)
        # res = 0
        # for idx in removable:
        #     removed.add(idx)
        #     if is_subsequence(s,p):
        #         res += 1
        # return res
        
        # optimization rather than linearly search in reomovable array apply binary search
        # Time: O(nlogk)
        # Space: O(k)
        
        def is_subsequence(_s,_p):
            i,j = 0,0
            while i < len(_s) and j < len(_p):
                if _s[i] != _p[j] or i in removed:
                    i+=1
                    continue
                i+=1
                j+=1
            return j == len(_p)
        
        res = 0
        start,end = 0,len(removable)-1
        while start <= end:
            mid = (start+end)//2
            removed = set(removable[:mid+1])
            if is_subsequence(s,p):
                res = max(res,mid+1)
                start = mid + 1
            else:
                end = mid - 1
        return res      
                    
                    
                
            