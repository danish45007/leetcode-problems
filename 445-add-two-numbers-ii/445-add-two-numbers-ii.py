# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_sum(head):
            list_sum = 0
            while head:
                list_sum = 10*list_sum + head.val
                head = head.next
            return list_sum
        total_sum = get_sum(l1) + get_sum(l2)
        dummy_list = ListNode(0)
        curr_node = dummy_list
        if total_sum == 0:
            return dummy_list
        while total_sum > 0:
            num = total_sum % 10
            curr_node.next = ListNode(num)
            curr_node = curr_node.next
            total_sum = total_sum // 10
        
        # reverse the linked list
        prev_node,curr_node,next_node = None,dummy_list.next,None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node