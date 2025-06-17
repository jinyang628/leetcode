# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        copy_2 = list2
        while copy_2.next:
            copy_2 = copy_2.next
        copy_1 = list1
        for _ in range(a - 1):
            copy_1 = copy_1.next
        tail_1 = copy_1
        for _ in range(b - a + 2):
            tail_1 = tail_1.next
        copy_1.next = list2
        copy_2.next = tail_1
        return list1