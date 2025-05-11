from collections import defaultdict, Counter
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr: list[int]) -> bool:
            max_element, min_element = max(arr), min(arr)
            r = max_element - min_element 
            if r % (len(arr) - 1) != 0:
                return False
            diff = r // (len(arr) - 1)
            counter = Counter(arr)
            curr = min_element
            iteration = 0
            while iteration < len(arr):
                print(counter, curr)
                if curr not in counter:
                    return False
                counter[curr] -= 1
                if not counter[curr]:
                    del counter[curr]
                curr += diff
                iteration += 1
            return True
        res = []
        for i in range(len(l)):
            res.append(
                check(nums[l[i]: r[i] + 1])
            )
        return res