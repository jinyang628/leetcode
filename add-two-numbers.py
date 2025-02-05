# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        res = ListNode(0)
        copy = res
        carry = 0
        while l1 and l2:
            print(res)
            print(l1)
            print(l2)
            total = l1.val + l2.val + carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            res.next = ListNode(total)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            total = l1.val + carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            res.next = ListNode(total)
            res = res.next
            l1 = l1.next
        while l2:
            total = l2.val + carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            res.next = ListNode(total)
            res = res.next
            l2 = l2.next
        if carry:
            res.next = ListNode(1)
        return copy.next