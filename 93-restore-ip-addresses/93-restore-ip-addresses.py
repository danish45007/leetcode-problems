class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # size of each ip bit from 0 to 256 and no leading 0's
        # if the length of the input string greater than 12 we can't form 4 bits using all the chars
        result = []
        if 4 > len(s) > 12:
            return result
        def backtrack(start_idx,dot_count,curr_ip):
            # base condition to get ip bit
            # created 4 bits using all the char in string
            if dot_count == 4 and start_idx == len(s):
                # triming the 4th bit before add to result
                result.append(curr_ip[:-1])
                return
            if dot_count > 4:
                return
            # to out bound case
            for j in range(start_idx,min(start_idx+3,len(s))):
                # len(s[start_idx:j+1]) == 1 or s[start_idx] != "0" this condition to check if there are no leading zeros if
                # length is 1 in that case its a single 0 which is valid or for other strat char should not be zero
                if(int(s[start_idx:j+1]) < 256 and (len(s[start_idx:j+1]) == 1 or s[start_idx] != "0")):
                    backtrack(j+1,dot_count+1,curr_ip + s[start_idx:j+1] + ".")
        backtrack(0,0,"")
        return result
            