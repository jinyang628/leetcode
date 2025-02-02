from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = deque([(endWord, 0)])
        def differs_by_one(s1: str, s2: str) -> bool:
            return sum(c1 != c2 for c1, c2 in zip(s1, s2)) == 1
        wordList = set(wordList)
        wordList.add(beginWord)
        while queue:
            currWord, currStep = queue.popleft()
            if currWord not in wordList:
                continue
            if currWord == beginWord:
                return currStep + 1
            wordList.remove(currWord)
            for i in range(len(currWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    candidateWord = currWord[:i] + c + currWord[i + 1:]
                    if candidateWord in wordList:
                        queue.append((candidateWord, currStep + 1))                    
        return 0