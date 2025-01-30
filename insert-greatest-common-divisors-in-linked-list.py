# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy = head
        while copy and copy.next:
            next_node = copy.next
            gcd = math.gcd(copy.val, next_node.val)
            copy.next = ListNode(gcd)
            copy = copy.next
            copy.next = next_node
            copy = copy.next
        return head