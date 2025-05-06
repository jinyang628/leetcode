# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        tailDummy = ListNode(0)
        headDummy = ListNode(0)
        copyHead = headDummy
        copyTail = tailDummy
        while head:
            if head.val < x:
                copyHead.next = head
                copyHead = copyHead.next
            else:
                copyTail.next = head
                copyTail = copyTail.next
            head = head.next
        copyTail.next = None
        copyHead.next = tailDummy.next
        return headDummy.next