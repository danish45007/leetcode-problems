class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        curr_word_index = 0
        curr_width = 0
        curr_line = []
        while curr_word_index < len(words):
            curr_word = words[curr_word_index]
            # if allowed to take the curr_word in curr_line
            if len(curr_word) + curr_width <= maxWidth:
                curr_line.append(curr_word)
                # plus 1 an extra space in ideal condition b/w each word
                curr_width += len(curr_word) + 1
                curr_word_index += 1
            else:
                spaces = maxWidth - curr_width + len(curr_line)
                # these spaces needs to go in b/w each word but not after the last word
                added = 0
                j = 0
                while added < spaces:
                    if j >= len(curr_line)-1:
                        j = 0
                    curr_line[j] += ' '
                    j +=1
                    added +=1 
                result.append(''.join(curr_line))
                curr_line = []
                curr_width = 0
        
        # processing the last line(last row)
        # first need to add white space b/w each word in line
        for i in range(len(curr_line)-1):
            if i < len(curr_line)-1:
                curr_line[i] += ' '
        
        # adding remaining white spaces at last
        spaces_need_to_added  = maxWidth - curr_width +1
        curr_line[-1] += ' '*spaces_need_to_added
        result.append(''.join(curr_line))
        return result