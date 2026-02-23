1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
67class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        slow = fast = head
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13            if not slow or not fast:
14                return False
15            if slow == fast:
16                return True
1718        return False