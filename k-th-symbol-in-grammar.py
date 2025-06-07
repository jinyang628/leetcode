class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        left = 0
        right = 2 ** (n - 1)
        curr = 0
        for _ in range(n - 1):
            mid = left + (right - left) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                curr = 0 if curr else 1
        return curr