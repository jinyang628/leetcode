from collections import Counter, defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        subseq = defaultdict(int)
        for num in nums:
            if not counter[num]:
                continue
            if subseq[num - 1]:
                subseq[num - 1] -= 1
                subseq[num] += 1
            elif counter[num + 1] and counter[num + 2]:
                counter[num + 1] -= 1
                counter[num + 2] -= 1
                subseq[num + 2] += 1
            else:
                return False
            counter[num] -= 1
        return True