# User function Template for python3

class Solution:
    def toh(self, N, s, d, h):
        count = 0
        # Your code here
        count +=1
        if N == 1:
            print("move disk {} from rod {} to rod {}".format(N,s,d))
            return count
        
        self.toh(N-1, s, h, d)
        print("move disk {} from rod {} to rod {}".format(N,s,d))
        count +=1
        self.toh(N-1, h, d, s)
        count +=1
        return count
        

#{ 
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends