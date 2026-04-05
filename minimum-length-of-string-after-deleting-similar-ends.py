1class Solution:
2    def minimumLength(self, s: str) -> int:
3        left_pointer, right_pointer = 0, len(s) - 1
4        while left_pointer < right_pointer:
5            if s[left_pointer] != s[right_pointer]:
6                break
7            curr = s[left_pointer]
8            while left_pointer < len(s) and s[left_pointer] == curr:
9                left_pointer += 1
10            while right_pointer >= 0 and s[right_pointer] == curr:
11                right_pointer -= 1
1213        if right_pointer < left_pointer:
14            return 0
15        return right_pointer - left_pointer + 1