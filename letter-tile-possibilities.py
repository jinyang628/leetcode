from collections import defaultdict, Counter
class Solution:
     def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(count: dict):
            total = 0
            for char in count:
                if count[char] == 0:
                    continue
                total += 1
                count[char] -= 1
                total += backtrack(count)
                count[char] += 1
            return total
        count = Counter(tiles)
        return backtrack(count)