# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth_node(k,curr):
            while curr and k > 0:
                curr = curr.next
                k -=1
            return curr
        
        dummy_node = ListNode(0,next=head)
        group_prev = dummy_node
        while True:
            kth = get_kth_node(k,group_prev)
            if not kth:
                break
            group_next = kth.next
            
            # reverse the group
            prev_node = kth.next
            curr_node=group_prev.next
            while curr_node != group_next:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        return dummy_node.next
                
                
                