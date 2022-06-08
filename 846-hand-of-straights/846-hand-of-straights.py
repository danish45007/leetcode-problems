class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count_map = {}
        heap = []
        for num in hand:
            count_map[num] = 1 + count_map.get(num,0)        
        for key in count_map:
            heapq.heappush(heap,key)
        
        while heap:
            min_element = heap[0]
            for ele in range(min_element,min_element+groupSize):
                if ele not in count_map:
                    return False
                count_map[ele] -=1
                if count_map[ele] == 0:
                    if(ele != heap[0]):
                        return False
                    else:
                        heapq.heappop(heap)
        return True
            