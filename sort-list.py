# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        if not a:
            return b
        if not b:
            return a
        dummy = ListNode(0)
        copy = dummy
        while a and b:
            if a.val <= b.val:
                copy.next = a
                a = a.next
            else:
                copy.next = b
                b = b.next
            copy = copy.next
        if a:
            copy.next = a
        if b:
            copy.next = b
        return dummy.next 
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        copy = slow
        if prev:
            prev.next = None
        left = self.sortList(head)
        right = self.sortList(copy)
        return self.merge(left, right)