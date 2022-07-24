class Solution:
    def bitwiseComplement(self, n: int) -> int:
        _sum = 1
        while _sum < n:
            _sum = _sum*2+1
        return _sum - n