from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        merged = []
        for i in range(len(values)):
            merged.append((values[i], labels[i]))
        label_taken = defaultdict(int)
        merged.sort(reverse=True)
        counter = res = 0
        for i in range(len(merged)):
            if label_taken[merged[i][1]] >= useLimit:
                continue 
            counter += 1
            res += merged[i][0]
            label_taken[merged[i][1]] += 1
            if counter == numWanted:
                break
        return res