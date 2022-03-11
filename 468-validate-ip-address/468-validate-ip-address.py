class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if(len(queryIP.split('.')) == 4 and all(self.is_valid_IPV4(bits) for bits in queryIP.split('.'))):
            return "IPv4"
        if(len(queryIP.split(':')) == 8 and all(self.is_valid_IPV6(bits) for bits in queryIP.split(':'))):
            print(all(self.is_valid_IPV6(bits) for bits in queryIP.split(':')))
            return "IPv6"
        return "Neither"
            
    
    def is_valid_IPV4(self,bits: str) -> bool:
        try:
            return str(int(bits)) == bits and 0 <= int(bits) <= 255
        except:
            return False
            
        
    def is_valid_IPV6(self,bits: str) -> bool:
        validAlphArea = ["a","A","b","B","c","C","d","D","e","E","f","F","1","2","3","4","5","6","7","8","9","0","-"]
        try:
            return ((1 <= len(bits) <= 4) and (all(bit in validAlphArea  for bit in bits)))
        except:
            return False
            
    
    
        