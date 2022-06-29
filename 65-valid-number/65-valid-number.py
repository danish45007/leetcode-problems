class Solution:
    def isNumber(self, s: str) -> bool:
        decimal_used = False
        number_seen = False
        signs = ['-','+']
        allowed_char = ['e','E']
        
        # check if the remaining string is valid int
        def valid_int(rem_string):
            if not rem_string:
                return False
            j = 0
            seen = False
            if rem_string[j] in signs:
                j += 1
            while j < len(rem_string):
                if not rem_string[j].isdigit():
                    return False
                else:
                    seen = True
                j+=1
            return seen
            
        
        i = 0
        if s[i] in signs: 
            i +=1
        while i < len(s):
            curr_char = s[i]
            # check for alph char
            if curr_char.isalpha():
                if curr_char not in allowed_char:
                    return False
                else:
                    print('fff')
                    # if in valid char list make sure there is valid number before and after char[e,E]
                    return number_seen and valid_int(s[i+1:])
            # check for decimal
            elif curr_char == '.':
                # decimal already seen 
                if decimal_used:
                    return False
                else:
                    decimal_used = True
            
            # check for sign
            # seen sign in b/w number
            elif curr_char in signs:
                return False
            # for actual number
            else:
                number_seen = True
            i +=1
        return number_seen
                    
        