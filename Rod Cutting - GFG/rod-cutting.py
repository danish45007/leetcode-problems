#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here
        length = [i for i in range(1,n+1)]
        dp = [[0 for j in range(len(price)+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(1,len(price)+1):
            dp[0][j] = 0
        for i in range(1,n+1):
            for j in range(1,len(length)+1):
                if(length[i-1] > j):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j],price[i-1]+dp[i][j-length[i-1]])
        return dp[n][len(price)]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends