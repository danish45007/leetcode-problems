class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uqiue_email_set = set()
        for email in emails:
            local,domain = email.split("@")
            space = []
            for char in local:
                if char == '.': continue
                if char == '+': break
                space.append(char)
            uqiue_email_set.add("".join(space) + '@' + domain)
            
        return len(uqiue_email_set)
        
            
        