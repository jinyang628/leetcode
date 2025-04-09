from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = deque([])
        queue.append((1, beginWord))
        visited = set()
        wordList.append(beginWord)
        neighbors = defaultdict(list) # key is the pattern, value is a list containing all the words that match that pattern
        def is_neighbor(a: str, b: str) -> bool:
            if len(a) != len(b):
                return False
            seen_diff = False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if seen_diff:
                        return False
                    seen_diff = True
            return seen_diff
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbors[pattern].append(word)
        while queue:
            dist, curr = queue.popleft()
            if curr == endWord:
                return dist 
            if curr in visited:
                continue
            visited.add(curr) 
            for i in range(len(curr)):
                pattern = curr[:i] + "*" + curr[i + 1:]
                for word in neighbors[pattern]:
                    queue.append((dist + 1, word))
        return 0