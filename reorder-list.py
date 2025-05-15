# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = slow.next
        slow.next = None
        prev = None
        while tail:
            next_node = tail.next
            tail.next = prev
            prev = tail
            tail = next_node
        first, second = head, prev
        while second:
            next_head, next_tail = first.next, second.next
            first.next = second
            second.next = next_head
            first, second = next_head, next_tail