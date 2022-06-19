class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        num_freq = {} #{num:count}
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num,0)
        heap = []
        for num in num_freq:
            heapq.heappush(heap,num)
        
        while heap:
            min_num = heap[0]
            # getting the consecutive num of the kth group starting from the min_num
            for num in range(min_num,min_num+k):
                # check if the num in nu_freq:
                if num not in num_freq:
                    return False
                else:
                    num_freq[num] -=1
                    if num_freq[num] == 0:
                        # check the alwways the min element is popped
                        if num != heap[0]:
                            return False
                        else:
                            heapq.heappop(heap)
        return True