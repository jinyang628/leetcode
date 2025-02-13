import heapq
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_to_block = defaultdict(list)
        block_to_prereqs = defaultdict(list)
        for block, prereq in prerequisites:
            prereq_to_block[prereq].append(block)
            block_to_prereqs[block].append(prereq)
        heap = []
        for i in range(numCourses):
            if not block_to_prereqs[i]:
                heapq.heappush(heap, i)
        res = 0
        while heap:
            curr = heapq.heappop(heap)
            res += 1
            blocked_courses = prereq_to_block[curr]
            for c in blocked_courses:
                block_to_prereqs[c].remove(curr)
                if not block_to_prereqs[c]:
                    heapq.heappush(heap, c)
        return res == numCourses