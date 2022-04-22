class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if("0" in [nums1,nums2]):
            return "0"
        # result array size will n + m where n is the size of nums1 and m is the size of nums2
        res = [0]*(len(nums1)+len(nums2))
        # reverse the nums as will multiplying the traditional way we start from the right to left
        nums1,nums2 = nums1[::-1],nums2[::-1]
        
        # iterating over the each digit in nums array
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                digit = int(nums1[i])*int(nums2[j])
                # add the digit in the right place of res 
                # root value of product of 2 numbers
                res[i+j] += digit
                # carry will moved to the next index
                # getting the carry from the curr result lsb
                res[i+j+1] += res[i+j]//10
                # getting the single digit msb of product of 2 digits
                res[i+j] = res[i+j]%10
        # reverse the result and remove the leading 0
        res = res[::-1]
        lead_zero=0
        #find the leading zero index and update result removing the leading zero
        while lead_zero < len(res) and res[lead_zero] == 0:
            lead_zero +=1
        # convert the arry into string
        res = map(str,res[lead_zero:])
        return "".join(res)
        
         
                
                