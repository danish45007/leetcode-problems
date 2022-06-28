class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = list(zip(startTime,endTime,profit))
        jobs.sort(key=lambda x:x[0])
        dp = {}
        def dfs(job_idx):
            # no job left to process therefore 0 profit
            if job_idx == n:
                return 0
            if job_idx in dp:
                return dp[job_idx]
            # take the profit of the curr job and go along the next job that just start after curr job end's
            next_job_idx = job_idx+1
            while next_job_idx < n and jobs[job_idx][1] > jobs[next_job_idx][0]:
                next_job_idx +=1
            choice_1 = jobs[job_idx][2] + dfs(next_job_idx)
            # skip the curr job and process the next job
            choice_2 = dfs(job_idx+1)
            max_profit = max(choice_1,choice_2)
            dp[job_idx] = max_profit
            return max_profit
        return dfs(0)