class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_taken_seat = None
        max_dist = float('-inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                # check for the first prev_taken_seat
                if prev_taken_seat == None:
                    max_dist = i
                else:
                    alex_seat = (i - prev_taken_seat)//2
                    max_dist = max(max_dist,alex_seat)
                prev_taken_seat = i
        # check for the right most empty seat
        return max(max_dist,(len(seats)-1)-prev_taken_seat)