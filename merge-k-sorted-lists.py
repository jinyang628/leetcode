# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        copy = dummy
        while True:
            idx_of_smallest_head = -1
            smallest_head_val = float('inf')
            should_terminate = True
            for i in range(len(lists)):
                curr = lists[i]
                if not curr:
                    continue
                should_terminate = False
                if curr.val < smallest_head_val:
                    idx_of_smallest_head = i
                    smallest_head_val = curr.val
            if should_terminate:
                break
            dummy.next = lists[idx_of_smallest_head]
            lists[idx_of_smallest_head] = lists[idx_of_smallest_head].next
            dummy = dummy.next
        return copy.next