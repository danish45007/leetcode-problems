class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        word_parser = s.split(' ')
        for i in range(len(word_parser)-1,-1,-1):
            if len(word_parser[i]) > 0:
                res.append(word_parser[i])
        return ' '.join(res)