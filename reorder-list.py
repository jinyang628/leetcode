# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        """
        if not head or not head.next:
            return 
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        second = None
        while slow:
            next_node = slow.next
            slow.next = second
            second = slow
            slow = next_node
        first = head
        while first and second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second
        copy = head
        while copy.next:
            copy = copy.next
        copy.next = second