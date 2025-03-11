# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, arr1: Optional[ListNode], arr2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        copy = dummy
        while arr1 and arr2:
            if arr1.val <= arr2.val:
                copy.next = arr1
                arr1 = arr1.next
            else:
                copy.next = arr2
                arr2 = arr2.next
            copy = copy.next
        if arr1:
            copy.next = arr1
        if arr2:
            copy.next = arr2
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        merged = self.merge(left, right)
        return merged