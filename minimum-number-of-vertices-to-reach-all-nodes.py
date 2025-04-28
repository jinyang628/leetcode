class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degrees = [0] * n
        for _, dst in edges:
            in_degrees[dst] += 1
        ans = []
        for i in range(len(in_degrees)):
            if not in_degrees[i]:
                ans.append(i)
        return ans