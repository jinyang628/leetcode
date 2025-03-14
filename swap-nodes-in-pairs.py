# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = head
        prev = dummy
        while left and left.next:
            right = left.next
            next_node = right.next
            prev.next = right            
            right.next = left
            left.next = next_node
            prev = left
            left = left.next
return dummy.next