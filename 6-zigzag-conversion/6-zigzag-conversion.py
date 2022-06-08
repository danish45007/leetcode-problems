class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        increment = (numRows - 1)*2
        for row in range(numRows):
            for i in  range(row,len(s),increment):
                # first and last row
                res += s[i]
                if(row > 0 and row < numRows-1 and  i+increment-2*row < len(s)):
                    # getting the intermedate char
                    res += s[i+increment-2*row]
        return res