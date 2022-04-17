# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # approach 2 using the slow,fast pointer 
        #get the middle node
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is pointing to the middle node
        # reverse the links of the second half of the linked list of direct comparision
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # start comparing the value from the start and end
        start,end = head,prev
        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        return True
            
            