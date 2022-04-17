# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        slow_pointer = dummy_node
        fast_pointer = head
        while n > 0:
            fast_pointer = fast_pointer.next
            n -=1
        while fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        # delete the target node
        slow_pointer.next = slow_pointer.next.next
        return dummy_node.next
            