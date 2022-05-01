def subset_with_given_diff(arr,diff):
    arr_sum = sum(arr)
    target_sum = (arr_sum + diff) // 2
    n = len(arr)
    zero_count = 0
    dp = [[0 for j in range(target_sum+1)] for i in range(n+1)]
    dp[0][0] = 1        
    for j in range(1,target_sum+1):
        dp[0][j] = 0
    
    for i in range(1,n+1):
        for j in range(target_sum+1):
            if(arr[i-1] > j):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    return dp[n][target_sum]
        


if __name__ == '__main__':
    print(subset_with_given_diff([1,1,2,3],1))