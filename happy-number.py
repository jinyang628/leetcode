1class Solution:
2    def isHappy(self, n: int) -> bool:
3        visited = set()
4        while n not in visited:
5            if n == 1:
6                return True
7            visited.add(n)
8            new_number = 0
9            for char in str(n):
10                new_number += int(char) ** 2
11            n = new_number
12        return False