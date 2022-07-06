class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binary_search(search_list,index):
            bin_res = -1
            l,r = 0,len(search_list)-1
            while l <= r:
                mid = (l+r)//2
                if search_list[mid] >= index:
                    bin_res = mid
                    r = mid-1
                else:
                    l = mid+1
            return bin_res
        
        intervals = sorted([[start,end,idx] for idx,[start,end] in enumerate(intervals)])
        start_time = [start_time for start_time,end_time,idx in intervals]
        res = [-1]*len(intervals)
        for interval in intervals:
            can_be_placed_idx = binary_search(start_time,interval[1])
            if can_be_placed_idx >= 0:
                res[interval[-1]] = intervals[can_be_placed_idx][-1]
        return res