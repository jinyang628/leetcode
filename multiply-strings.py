1class Solution:
2    def multiply(self, num1: str, num2: str) -> str:
3        res = []
4        outer_ten_multiplier = 1
5        for outer_char in num1[::-1]:
6            inner_ten_multiplier = 1
7            for inner_char in num2[::-1]:
8                res.append(
9                    int(outer_char) * int(inner_char) * outer_ten_multiplier * inner_ten_multiplier
10                )
11                inner_ten_multiplier *= 10
12            outer_ten_multiplier *= 10
13        return str(sum(res))
1415