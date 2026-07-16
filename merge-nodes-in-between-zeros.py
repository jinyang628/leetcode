1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        start = False
9        dummy = ListNode(0)
10        copy = dummy
11        running_sum = 0
12        while head:
13            if head.val == 0:
14                if not start:
15                    start = True
16                else:
17                    dummy.next = ListNode(running_sum)
18                    running_sum = 0
19                    dummy = dummy.next
20            else:
21                running_sum += head.val
22            head = head.next
232425        return copy.next