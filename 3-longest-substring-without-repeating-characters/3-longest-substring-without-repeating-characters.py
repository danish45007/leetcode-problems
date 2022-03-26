class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _map = {}
        i,j = 0,0
        _max = 0
        while j < len(s):
            if s[j] in _map:
                _map[s[j]] += 1
            else:
                _map[s[j]] = 1
            
            if(len(_map) == (j-i+1)):
                _max = max(_max,(j-i+1))
                j+=1
            elif(len(_map) < (j-i+1)):
                while len(_map) < (j-i+1):
                    _map[s[i]] -=1
                    
                    if(_map[s[i]] == 0):
                        del _map[s[i]]
                    
                    i+=1
                j+=1
        return _max
                