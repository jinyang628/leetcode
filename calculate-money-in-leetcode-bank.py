1class Solution:
2    def totalMoney(self, n: int) -> int:
3        full_sets = n // 7
4        remainder = n - (full_sets * 7)
5        remainder_sum = int((full_sets + 1 + full_sets + remainder) * (remainder / 2))
6        full_set_sum = int((28 + 28 + (7 * (full_sets - 1))) * (full_sets / 2))
7        return remainder_sum + full_set_sum
8