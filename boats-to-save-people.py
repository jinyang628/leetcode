1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        left, right = 0, len(people) - 1  
5        res = 0
6        while left < right:
7            if people[left] + people[right] <= limit:
8                left += 1
9                right -= 1
10            else:
11                right -= 1
12            res += 1
13        if left == right:
14            res += 1
15        return res