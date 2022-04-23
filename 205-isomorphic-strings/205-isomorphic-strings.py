class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        _map = {}
        if len(t) != len(s) or len(set(s)) != len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] not in _map:
                _map[s[i]] = t[i]
            elif _map[s[i]] != t[i]:
                return False
        return True