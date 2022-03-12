def sorted(s):
    def sort_stack_recursive(stack):
        if(len(stack) == 1):
            return stack
        first_element = stack.pop(0)
        sort_stack_recursive(stack)
        return insert_into_stack(stack,first_element)

    def insert_into_stack(stack,num):
        if len(stack) == 0 or stack[0] <= num:
            stack.insert(0,num)
            return stack
        first_element = stack.pop(0)
        insert_into_stack(stack,num)
        stack.insert(0,first_element)
        return stack
    return sort_stack_recursive(s)
        
print(sorted([3,2,1]))