class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        startPrefixSums = [0]
        for i in range(k):
            startPrefixSums.append(cardPoints[i] + startPrefixSums[i])
        endPrefixSums = [0]
        for i in range(k):
            endPrefixSums.append(cardPoints[-1 * (i + 1)] + endPrefixSums[i])
        res = 0
        for num_left in range(k + 1):
            res = max(
                res, 
                startPrefixSums[num_left] + endPrefixSums[k - num_left]
            )
        return res