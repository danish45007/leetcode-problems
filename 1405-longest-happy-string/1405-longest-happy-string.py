class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # going greedy
        max_heap = [] #(count,char)
        char_count = [(-a,'a'),(-b,'b'),(-c,'c')]
        for count,char in char_count:
            if count != 0:
                heapq.heappush(max_heap,(count,char))
        res = []
        while max_heap:
            # get the most freq one
            count,char = heapq.heappop(max_heap)
            # check if the char is same as prev two in res
            if len(res) > 1 and res[-1] == char and res[-2] == char:
                if not max_heap:
                    break
                # pop out the another char
                count_2,char_2 = heapq.heappop(max_heap)
                res.append(char_2)
                count_2 +=1
                if count_2:
                    heapq.heappush(max_heap,(count_2,char_2))
            else:
                res.append(char)
                count +=1
            if count:
                heapq.heappush(max_heap,(count,char))
        return ''.join(res)
        