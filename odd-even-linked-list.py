# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = ListNode(0)
        even = ListNode(0)
        copy_odd = odd
        copy_even = even
        copy = head
        is_odd = True
        while copy:
            if is_odd:
                copy_odd.next = copy
                copy_odd = copy_odd.next
            else:
                copy_even.next = copy
                copy_even = copy_even.next
            copy = copy.next
            is_odd = not is_odd
        if is_odd:
            copy_odd.next = None
        else:
            copy_even.next = None
        copy = odd 
        while copy.next:
            copy = copy.next
        copy.next = even.next
        return odd.next