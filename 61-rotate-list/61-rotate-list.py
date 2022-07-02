# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # getting the length of linked list and the tail node
        tail = head
        length = 1
        while tail.next:
            length +=1
            tail = tail.next
        
        k = k % length
        if k == 0:
            return head
        
        # breaking the linked list at the pivot(length-k-1) and pointer the node before pivot to None(tail)
        pivot = head
        for i in range(length-k-1):
            pivot = pivot.next
        new_head = pivot.next
        pivot.next = None
        tail.next = head
        return new_head