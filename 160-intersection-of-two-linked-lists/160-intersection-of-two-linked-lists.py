# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_list_size(head):
            start = head
            size = 0
            while start:
                start = start.next
                size += 1
            return size
        size_a = get_list_size(headA)
        size_b = get_list_size(headB)
        size_diff = abs(size_a-size_b)
        
        # increment the start by the size diff of the larger list
        start_a,start_b = headA,headB
        if(size_a > size_b):
            for i in range(size_diff):
                start_a = start_a.next
        elif(size_a < size_b):
            for i in range(size_diff):
                start_b = start_b.next
        while start_a and start_b:
            if start_a == start_b:
                return start_a
            start_a = start_a.next
            start_b = start_b.next
        else:
            return None
                
                