from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hierarchy = defaultdict(list) # key is supervisor, value is subordinate list
        for i in range(len(manager)):
            hierarchy[manager[i]].append(i)
        def dfs(person: int) -> int:
            if not hierarchy[person]:
                return 0
            return informTime[person] + max(dfs(subordinate) for subordinate in hierarchy[person])
        print(hierarchy)
        return dfs(headID)