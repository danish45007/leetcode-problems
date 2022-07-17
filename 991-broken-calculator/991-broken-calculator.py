class Solution:
    def brokenCalc(self, start: int, target: int) -> int:
        # going in the opposite way from target -> start
        '''
            operations:
                1. divide:  / 2
                2. add: +1
        '''
        operations = 0
        while target > start:
            operations +=1
            # even
            if target % 2 == 0:
                target = target // 2
            else:
                target = target + 1
        return operations + (start-target)