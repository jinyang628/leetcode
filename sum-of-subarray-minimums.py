1class Solution:
2    def sumSubarrayMins(self, arr: List[int]) -> int:
3        stack = []
4        res = [0] * len(arr)
5        for i in range(len(arr)):
6            while stack and arr[stack[-1]] > arr[i]:
7                stack.pop()
89            prevSmallestIdx = stack[-1] if stack else - 1
10            res[i] = (i - prevSmallestIdx) * arr[i] + res[prevSmallestIdx]
11            stack.append(i)
1213        return sum(res) %(10**9 + 7)