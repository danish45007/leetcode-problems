class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_index_map = defaultdict(list)
        for i,char in enumerate(s):
            char_index_map[char].append(i)
        res = 0
        def binary_search(search_list,index):
            bin_res = -1
            l,r = 0,len(search_list)-1
            while l <= r:
                mid = (l+r)//2
                if search_list[mid] > index:
                    bin_res = mid
                    r = mid-1
                else:
                    l = mid+1
            return bin_res
                    
        for word in words:
            prev_index = -1
            found = True
            for char in word:
                if binary_search(char_index_map[char],prev_index) >= 0:
                    prev_index = char_index_map[char][binary_search(char_index_map[char],prev_index)]
                else:
                    found = False
                    break
            if found:
                res += 1
        return res
        

