1class Solution:
2    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
3        a = b = c = False
4        for first, second, third in triplets:
5            if first == target[0] and second <= target[1] and third <= target[2]:
6                a = True
7            if second == target[1] and first <= target[0] and third <= target[2]:
8                b = True
9            if third == target[2] and first <= target[0] and second <= target[1]:
10                c = True
111213        return a and b and c