def solve(stack):
    size = len(stack)
    def reverse_stack(stack,size):
        print(size)
        if(size == 0):
            return
        top_element = stack.pop(0)
        reverse_stack(stack,size-1)
        stack.append(top_element)
        return stack
    return reverse_stack(stack,size)

print(solve([4,5,6,7,8,8,9,9,9,0,0,0]))