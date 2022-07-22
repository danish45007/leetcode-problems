# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def get_number_from_list(head):
            list_sum = 0
            while head:
                list_sum = 10*list_sum + head.val
                head = head.next
            return list_sum
        def get_binary_to_decimal(binary):
            num = 0
            for i in range(len(binary)):
                num += 2**i * int(binary[i])
            return num
        
        binary = get_number_from_list(head)
        binary = str(binary)[::-1]
        return get_binary_to_decimal(binary)