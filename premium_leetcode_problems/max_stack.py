'''

Description
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.



Input:
push(5)
push(1)
push(5)
top()
popMax()
top()
peekMax()
pop()
top()
Output:
5
5
1
5
1
5

'''


from collections import deque
class MaxStack:
    
    def __init__(self):
        # do intialization if necessary
       self.stack = []
       self.max_stack = []
       self.queue = deque()
    
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
       self.stack.append(x)
       max_val = max(x,self.max_stack[-1] if self.max_stack else x)
       self.max_stack.append(max_val)

    """
    @return: An integer
    """
    def pop(self):
        # while poping from the stack pop
        # from both  stack and max_stack
        top = self.stack.pop()
        self.max_stack.pop()
        return top


    """
    @return: An integer
    """
    def top(self):
        # write your code here
        # return the last element of stack
       return self.stack[-1]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        # return the last element of max_stack
       return self.max_stack[-1]

    """
    @return: An integer
    """
    def popMax(self):
        # write your code here
        # get the current max and stack pop the all elements from 
        # stack and max_stack and appending then into queue while don't reach the max 
        # after we exist from the while loop start appending the element back to queue using the push method
        current_max = self.max_stack[-1]
        current_index = len(self.stack) - 1
        while self.stack[current_index] != current_max:
           self.queue.append(self.stack.pop())
           self.max_stack.pop() 
           current_index -= 1
        if self.stack[current_index] == current_max:
            self.stack.pop()
            self.max_stack.pop() 
        while self.queue:
            self.push(self.queue.pop())
        return current_max
        

    