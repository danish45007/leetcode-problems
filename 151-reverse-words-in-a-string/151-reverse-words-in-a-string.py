class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        rev_list = s.split(' ')
        for i in range(len(rev_list)-1,-1,-1):
            if len(rev_list[i]) > 0:
                res.append(rev_list[i])
        return ' '.join(res)