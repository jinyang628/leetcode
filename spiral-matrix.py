1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        left = top = 0
4        right = len(matrix[0]) - 1
5        bottom = len(matrix) - 1
6        res = []
7        while left <= right and top <= bottom:
8            original_left = left
9            while left <= right:
10                res.append(matrix[top][left])
11                left += 1
12            left = original_left
13            top += 1
14            original_top = top
15            while top <= bottom:
16                res.append(matrix[top][right])
17                top += 1
18            top = original_top
19            right -= 1
20            original_right = right
21            if not left <= right or not top <= bottom:
22                break
23            while right >= left:
24                res.append(matrix[bottom][right])
25                right -= 1
26            right = original_right
27            bottom -= 1
28            original_bottom = bottom
29            while bottom >= top:
30                res.append(matrix[bottom][left])
31                bottom -= 1
32            bottom = original_bottom
33            left += 1
343536        return res
373839