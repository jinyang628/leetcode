# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy = head
        while copy and copy.next:
            if copy.next.val != copy.val:
                copy = copy.next
            else:
                copy.next = copy.next.next
        return head