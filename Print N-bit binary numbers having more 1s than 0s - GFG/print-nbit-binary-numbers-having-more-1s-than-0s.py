#User function Template for python3
class Solution:
	def NBitBinary(self, N):
		# code here
		ones = 0
		zeros = 0
		out = []
		res = []
		return self.solve(ones,zeros,N,out,res)
	def solve(self,ones,zeros,n,out,res):
	    if n == 0:
	        res.append(''.join(char for char in out))
	        return
	    # pushing 1
	    out1 = out.copy()
	    out1.append('1')
	    self.solve(ones+1,zeros,n-1,out1,res)
	    if(ones > zeros):
	        out2 = out.copy()
	        out2.append('0')
	        self.solve(ones,zeros+1,n-1,out2,res)
	    return res
	        
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends