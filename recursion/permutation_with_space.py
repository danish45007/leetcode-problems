def permutation(S):
        # code here
        if(len(S) == 1):
            return [S]
        result = []
        sub = [S[0]]
        S = S[1:]
        print(sub,S)
        
        def solve(i,o,res):
            if(len(i) == 0):
                r = ''.join([str(elem) for elem in o])
                res.append(r)
                return res
            o1 = o.copy()
            o2 = o.copy()
            space_out = " {}".format(i[0])
            o1.append(space_out)
            o2.append(i[0])
            i = i[1:]
            solve(i,o1,res)
            solve(i,o2,res)
            return res
        
        return solve(S,sub,result)

print(permutation("AA"))