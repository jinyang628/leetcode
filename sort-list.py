1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head: 
9            return None
10        if not head.next:
11            return head
12        slow = fast = head
13        prev = slow
14        while fast and fast.next:
15            fast = fast.next.next
16            prev = slow
17            slow = slow.next
1819        prev.next = None
20        sorted_a = self.sortList(head)
21        sorted_b = self.sortList(slow)
2223        return self.merge(sorted_a, sorted_b)
2425    def merge(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
26        dummy = ListNode(0)
27        copy = dummy
28        if not a:
29            return b
30        if not b:
31            return a
32        while a and b:
33            if a.val <= b.val:
34                dummy.next = ListNode(a.val)
35                a = a.next
36            else:
37                dummy.next = ListNode(b.val)
38                b = b.next
39            dummy = dummy.next
4041        if a:
42            dummy.next = a
4344        if b:
45            dummy.next = b
4647        return copy.next