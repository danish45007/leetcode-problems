#User function Template for python3

class Solution:
    def safePos(self, n, k):
        person = []
        for i in range(1,n+1):
            person.append(i)
        k = k-1
        index = 0
        return self.solve(person,k,index)
    def solve(self,person,k,index):
        if len(person) == 1:
            return person[0]
        
        index = (index + k) % len(person)
        person = person[:index] + person[index+1:]
        return self.solve(person,k,index)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,k=map(int,input().split())
        
        ob = Solution()
        print(ob.safePos(n,k))
# } Driver Code Ends