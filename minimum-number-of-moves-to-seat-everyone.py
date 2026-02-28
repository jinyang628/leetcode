1class Solution:
2    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
3        seats.sort()
4        students.sort()
5        res = 0
6        for i in range(len(seats)):
7            res += abs(seats[i] - students[i])
8        return res