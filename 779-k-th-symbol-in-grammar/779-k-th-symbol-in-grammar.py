class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        bit_size = 2**(n-1)
        print(bit_size)
        mid = bit_size//2
        if(k <= mid):
            return self.kthGrammar(n-1,k)
        else:
            return int(not self.kthGrammar(n-1,k-mid))