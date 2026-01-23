1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        carry = 1
4        for i in range(len(digits) - 1, -1, -1):
5            curr = digits[i] + carry
6            if curr == 10:
7                carry = 1
8                curr = 0
9            else:
10                carry = 0
11            digits[i] = curr
12        if carry == 1:
13            return [1] + digits
14        return digits
15