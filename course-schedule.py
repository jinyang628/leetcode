from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_to_block = defaultdict(list)
        block_to_prereq = defaultdict(set)
        for a, b in prerequisites:
            prereq_to_block[b].append(a)
            block_to_prereq[a].add(b)
        stack = []
        for i in range(numCourses):
            if not block_to_prereq[i]:
                stack.append(i)
        visited = set()
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for block in prereq_to_block[curr]:
                block_to_prereq[block].remove(curr)
                if not block_to_prereq[block]:
                    stack.append(block)
        return len(visited) == numCourses