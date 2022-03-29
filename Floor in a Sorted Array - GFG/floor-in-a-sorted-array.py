class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,N,A,X):
        #Your code here
        start = 0
        end = len(N) - 1
        res = -1
        while start <= end:
            mid = start + (end-start) // 2
            if(N[mid] == X):
                return mid
            if(N[mid] <= X):
                res = mid
                start = mid +1
            if(N[mid] >= X):
                end = mid - 1
        return res
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends