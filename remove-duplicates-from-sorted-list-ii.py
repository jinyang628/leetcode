# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        copy_dummy = dummy
        copy = head
        duplicates = set()
        while copy:
            if copy.next:
                if copy.val == copy.next.val:
                    duplicates.add(copy.val)
            copy = copy.next
        copy = head
        while copy: 
            if copy.val not in duplicates:
                copy_dummy.next = copy
                copy_dummy = copy_dummy.next
            else:
                copy_dummy.next = copy.next
            copy = copy.next 
        return dummy.next