class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = list(str(n))
    
        if len(n) > 3:
            for i in range(len(n)-3 , 0 , -3 ):
                n.insert(i ,'.')
        return ''.join(n)