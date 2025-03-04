"""
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        track = {}
        copy_head = head
        while copy_head:
            track[copy_head] = Node(copy_head.val)
            copy_head = copy_head.next
        copy_head = head
        while copy_head:
            if copy_head.next:
                track[copy_head].next = track[copy_head.next]
            if copy_head.random:
                track[copy_head].random = track[copy_head.random]
            copy_head = copy_head.next
        return track[head]