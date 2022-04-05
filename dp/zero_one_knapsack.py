def zero_one_knapsack(wt,val,W,n):
    memo = [[-1 for i in range(W+1)] for j in range(n+1)]
    if(n == 0 or W == 0):
        return 0
    if(memo[n][W] != -1):
        return memo[n][W]
    if(wt[n-1] <= W):
        memo[n][W] = max(val[n-1] + zero_one_knapsack(wt,val,W-wt[n-1],n-1),zero_one_knapsack(wt,val,W,n-1))
        return memo[n][W]
    else:
        memo[n][W] = zero_one_knapsack(wt,val,W,n-1)
        return memo[n][W]


if __name__ == "__main__":
    wt = [10, 20, 30]
    val = [60, 100, 120]
    W=50
    n=len(wt)
    print(zero_one_knapsack(wt,val,W,n))