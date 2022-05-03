class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = {}
        def helper(i,day):
            if i >= n:
                return 0
            if (i,day) in dp:
                return dp[(i,day)]
            ans = float('inf')
            if days[i] > day:
                ans = min(ans,costs[0]+helper(i+1,days[i]))
                ans = min(ans,costs[1]+helper(i+1,days[i]+6))
                ans = min(ans,costs[2]+helper(i+1,days[i]+29))
            else:
                ans = min(ans,helper(i+1,day))  
            dp[(i,day)] = ans
            return ans


        a = helper(0,0)

        return a
                
        