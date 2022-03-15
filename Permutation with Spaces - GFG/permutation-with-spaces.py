#User function Template for python3

class Solution:
    def permutation (self, S):
        # code here
        if(len(S) == 1):
            return [S]
        result = []
        sub = [S[0]]
        S = S[1:]
        return self.solve(S,sub,result)
    
    
    def solve(self,i,o,res):
    
        if(len(i) == 0):
            r = ''.join([str(elem) for elem in o])
            res.append(r)
            return
        o1 = o.copy()
        o2 = o.copy()
        space_out = " {}".format(i[0])
        o1.append(space_out)
        o2.append(i[0])
        
        i = i[1:]
        self.solve(i,o1,res)
        self.solve(i,o2,res)
        return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends