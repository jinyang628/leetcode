# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head_list1 = list1
        for _ in range(a - 1):
            list1 = list1.next
        tail_list1 = list1
        for _ in range(b - a + 2):
            tail_list1 = tail_list1.next
        head_list2 = list2
        while list2.next:
            list2 = list2.next
        list1.next = head_list2
        list2.next = tail_list1
        return head_list1