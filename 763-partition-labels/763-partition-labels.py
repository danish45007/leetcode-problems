class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        size,end = 0,0
        # char to last index map
        last_index_map = {}
        for i,c in enumerate(s):
            last_index_map[c] = i
        
        
        for index,char in enumerate(s):
            last_index = last_index_map[char]
            size += 1
            end = max(end,last_index)
            # reached the end of the Partition where all the elements(indexs) are within end (<= end)
            # now we can create a new Partition
            if index == end:
                result.append(size)
                size = 0
        return result
            