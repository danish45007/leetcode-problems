#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        max_size = 0
        _map = {}
        i,j = 0,0
        if(len(set(s)) < k):
            return -1
        while j < len(s):
            if s[j] in _map:
                _map[s[j]] +=1
            else:
                _map[s[j]] = 1
            
            if len(_map) < k:
                j += 1
            elif len(_map) == k:
                max_size = max(max_size,(j-i+1))
                j +=1
            else:
                while len(_map) > k:
                    _map[s[i]] -=1
                    if(_map[s[i]] == 0):
                        del _map[s[i]]
                    i += 1
                j +=1
        return max_size

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends