1class Solution:
2    def maxScore(self, cardPoints: List[int], k: int) -> int:
3        if k == len(cardPoints):
4            return sum(cardPoints)
5        left_pointer = len(cardPoints) - k
6        maxSoFar = curr = sum(cardPoints[left_pointer:])
7        right_pointer = -1
8        while right_pointer < k - 1:
9            right_pointer += 1
10            curr += cardPoints[right_pointer]
11            curr -= cardPoints[left_pointer]
12            left_pointer += 1
13            maxSoFar = max(maxSoFar, curr)
14        return maxSoFar