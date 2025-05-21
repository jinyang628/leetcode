class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        prefixSums = [1] * n
        for _ in range(k):
            for i in range(1, len(prefixSums)):
                prefixSums[i] += prefixSums[i - 1]
        return prefixSums[-1] % (10 ** 9 + 7)