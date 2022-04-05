def zero_one_knapsack_bottom_up(wt,val,W,n):
    # initalizing matrix n*W
    t = [[None for j in range(W+1)] for i in range(n+1)]
    # transforming the 0th row and 0th column with zero
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                t[i][w] = 0
            elif wt[i-1] <= w: 
                t[i][w] = max(val[i-1] + t[i-1][w-wt[i-1]],  t[i-1][w]) 
            else: 
                t[i][w] = t[i-1][w] 
  
    return t[n][W] 
                


if __name__ == "__main__":
    wt = [10, 20, 30]
    val = [60, 100, 120]
    W=50
    n=len(wt)
    print(zero_one_knapsack_bottom_up(wt,val,W,n))