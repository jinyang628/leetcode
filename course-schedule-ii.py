from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        blocked_to_prereq = defaultdict(set) # key is blocked course, value is prereq
        prereq_to_blocked = defaultdict(set) # key is prereq, value is the course it blocks
        for blocked, prereq in prerequisites:
            blocked_to_prereq[blocked].add(prereq)
            prereq_to_blocked[prereq].add(blocked)
        res = []
        stack = []
        for i in range(numCourses):
            if not blocked_to_prereq[i]:
                stack.append(i)
        while stack:
            curr = stack.pop()
            res.append(curr)
            for c in prereq_to_blocked[curr]:
                blocked_to_prereq[c].remove(curr)
                if not blocked_to_prereq[c]:
                    stack.append(c)
        return res if len(res) == numCourses else []