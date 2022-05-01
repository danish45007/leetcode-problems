#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        _sum,_max_sum = 0,0
        i,j = 0,0
        while j < len(Arr):
            _sum = _sum + Arr[j]
            if(j-i+1 < K):
                j += 1
            elif(j-i+1 == K):
                _max_sum = max(_max_sum,_sum)
                _sum = _sum - Arr[i]
                i +=1
                j +=1
        
        return _max_sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends


