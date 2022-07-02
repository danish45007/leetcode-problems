class Solution:
    def arrangeWords(self, text: str) -> str:
        word_length_map = defaultdict(list)
        text = text.split(' ')
        min_count = float('inf')
        for word in text:
            word_length = len(word)
            min_count = min(min_count,word_length)
            word_length_map[word_length].append(word.lower())
        res = []
        first_word_marked = False
        for key in sorted(word_length_map.keys()):
            for word in word_length_map[key]:
                if key == min_count and not first_word_marked:
                    res.append(word[0].upper() + word[1:])
                    first_word_marked = True
                else:
                    res.append(word)
        return ' '.join(res)
            