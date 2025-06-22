# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 0
        copy = head
        while copy:
            length += 1
            copy = copy.next    
        if not k % length:
            return head
        copy = head
        for _ in range(length - (k % length) - 1):
            copy = copy.next
        new_head = copy.next
        copy.next = None
        copy_head = new_head
        while copy_head.next:
            copy_head = copy_head.next
        copy_head.next = head
        return new_head