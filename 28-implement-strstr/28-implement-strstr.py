class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # brute force
        # if len(haystack) == 0: return 0
        # for i in range(len(haystack)+1-len(needle)):
        #     for j in range(len(needle)):
        #         print(haystack[i+j],j)
        #         if haystack[i+j] != needle[j]:
        #             break
        #         # reached the last index of needle
        #         if j == len(needle)-1:
        #             return i
        # return -1
        
        # KMP
        if needle == '':
            return 0
        
        lps = [0] * len(needle)
        prev_lps_ptr = 0
        curr_ptr = 1
        while curr_ptr < len(needle):
            if needle[curr_ptr] == needle[prev_lps_ptr]:
                lps[curr_ptr] = prev_lps_ptr + 1
                prev_lps_ptr += 1
                curr_ptr +=1
            else:
                if prev_lps_ptr == 0:
                    lps[curr_ptr] = 0
                    curr_ptr+=1
                else:
                    prev_lps_ptr = lps[prev_lps_ptr-1]
        i = 0 # ptr for haystack
        j = 0 # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i +=1
                j +=1
            else:
                if j == 0:
                    i +=1
                else:
                    j = lps[j-1]
            
            if j == len(needle):
                return i - j
        return -1
                
        
                
                
                