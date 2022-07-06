# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        prev = dummy_node
        curr = head
        # atleast 2 node to swap
        while curr and curr.next:
            # next pair
            next_pair = curr.next.next
            # second node in first pair
            # it will be new head now so dummy.next will point to second
            # curr is the first node in the pair and after swap it will become the the second so new second will point the curr
            second = curr.next
            prev.next = second
            second.next = curr
            curr.next = next_pair
            # update pointers
            prev = curr
            curr = next_pair
        return dummy_node.next