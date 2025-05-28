# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        copy = head 
        length = 0
        while copy:
            length += 1
            copy = copy.next
        seg_len = math.floor(length / k)
        spill_over = length % k
        lengths = [seg_len] * k
        for i in range(spill_over):
            lengths[i] += 1
        res = []
        counter = 0
        length_counter = -1
        while len(res) != k:
            length_counter += 1
            if not head:
                res.append(None)
                continue
            new_seg = head
            new_seg_copy = new_seg
            for _ in range(lengths[length_counter]):
                prev = new_seg
                new_seg = new_seg.next
            prev.next = None
            head = new_seg
            res.append(new_seg_copy)
        return res