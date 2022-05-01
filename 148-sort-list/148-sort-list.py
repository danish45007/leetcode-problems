# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)
    
    def merge_sort(self,head):
        if not head or not head.next:
            return head
        left = head
        # middle node
        right = self.get_mid(head)
        print(right.val)
        # break the pointer b/w left and right
        temp = right.next
        right.next = None
        right = temp
        l = self.merge_sort(left)
        r = self.merge_sort(right)
        return self.merge_sorted_list(l,r)
    
    def get_mid(self,head):
        # fast starting from hed.next coz we want to end prev to mid
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge_sorted_list(self,l1,l2):
        dummy_node = ListNode()
        tail = dummy_node
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy_node.next