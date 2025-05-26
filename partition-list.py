# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        right = ListNode(0)
        copy = head
        copy_left = left
        copy_right = right
        while copy:
            if copy.val < x:
                copy_left.next = copy
                copy_left = copy_left.next
            else:
                copy_right.next = copy
                copy_right = copy_right.next
            copy = copy.next
        copy_right.next = None
        copy_left.next = right.next
        return left.next