class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        singles = {"b", "a", "n"}
        doubles = {"l", "o"}
        minSingles = float('inf')
        minDoubles = float('inf')
        visited = set()
        for key, val in count.items():
            if key in singles:
                visited.add(key)
                minSingles = min(minSingles, val)
            if key in doubles:
                visited.add(key)
                minDoubles = min(minDoubles, val)
        if len(visited) != 5:
            return 0
        if minSingles == float('inf') or minDoubles == float('inf'):
            return 0
        return min(minSingles, minDoubles // 2)