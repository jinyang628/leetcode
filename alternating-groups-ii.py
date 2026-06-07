1class Solution:
2    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
3        res = 0
4        for i in range(k - 1):
5            colors.append(colors[i])
6        left = 0
7        right = 1
8        while right < len(colors):
9            if colors[right] == colors[right - 1]:
10                left = right
11            if right - left + 1 == k:
12                res += 1
13                left += 1
14            right += 1
1516        return res