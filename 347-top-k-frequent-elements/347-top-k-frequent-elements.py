class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count to value map
        # key will the possible counts in array and value as array of vlaues against count
        # hash_map = {}
        # res = []
        # for num in nums:
        #     hash_map[num] = 1 + hash_map.get(num,0)
        # count_map = [[] for i in range(len(nums)+1)]
        # for key,val in hash_map.items():
        #     count_map[val].append(key)
        # print(count_map)
        # for i in range(len(count_map)-1,0,-1):
        #     if len(count_map[i]) > 0:
        #         for n in count_map[i]:
        #             res.append(n)
        #         if len(res) == k:
        #             return res
            
        freq_count = {}
        for num in nums:
            freq_count[num] = 1 + freq_count.get(num,0)
        count_values = [[] for i in range(len(nums)+1)]
        
        for num,count in freq_count.items():
            count_values[count].append(num)
        res = []
        for i in range(len(count_values)-1,-1,-1):
            if len(count_values[i]) > 0:
                for n in count_values[i]:
                    res.append(n)
                if len(res) == k:
                    return res
                
            
            
            
        
        
        
            