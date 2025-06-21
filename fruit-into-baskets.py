from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = maxSoFar = 0
        counter = Counter()
        while right < len(fruits):
            counter[fruits[right]] += 1
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if not counter[fruits[left]]:
                    del counter[fruits[left]]
                left += 1
            maxSoFar = max(maxSoFar, right - left + 1)
            right += 1
        return maxSoFar