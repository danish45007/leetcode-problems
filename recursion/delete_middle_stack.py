def solve(stack):
    if(len(stack) % 2 == 0):
        middle = (len(stack) // 2) + 1
    else:
        middle = (len(stack) + 1) // 2
        
    def delete_middle_element(stack,k):
        # base condition
        if (k == 1):
            stack.pop(0)
            return
        # hypothesis
        top = stack.pop(0)
        delete_middle_element(stack,k-1)
        # induction
        stack.insert(0,top)
        return stack
        
    
    return delete_middle_element(stack,middle)

print(solve([5,4,3,2,1]))