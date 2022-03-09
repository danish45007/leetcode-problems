class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        input_string = s
        output_string = ""
        result = []
        self.solve(input_string,output_string,result)
        return result
    def solve(self,input_string,output_string,result):
    #base-condition
        if(len(input_string) == 0):
            result.append(output_string)
            return

        if(input_string[0].isalpha()):
            output_string_1 = output_string
            output_string_2 =  output_string
            output_string_1 += input_string[0].lower()
            output_string_2 += input_string[0].upper()
            input_string = input_string[1:]
            self.solve(input_string,output_string_1,result)
            self.solve(input_string,output_string_2,result)
        else:
            output_string += input_string[0]
            input_string = input_string[1:]
            self.solve(input_string,output_string,result)
        
        
        
        
        
        
       
        