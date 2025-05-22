class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        for a, b in costs:
            arr.append((a - b,a, b))
        arr.sort()
        res = 0
        for i in range(len(arr)):
            if i < len(arr) // 2:
                res += arr[i][1]
            else:
                res += arr[i][2]
        return res