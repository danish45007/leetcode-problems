class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        valid_k_unit_place__values = set([1,3,7,9])
        if k%10 not in valid_k_unit_place__values:
            return -1
        length = 1
        num = 1 #[1,11,111,1111]
        while True:
            if num % k == 0:
                return length
            length +=1
            num = 10*num + 1