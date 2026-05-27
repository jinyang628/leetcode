1from collections import deque
2class Solution:
3    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
4        deck.sort()
5        queue = deque([i for i in range(len(deck))])
6        res = [0] * len(deck)
7        counter = 0
8        while queue:
9            curr = queue.popleft()
10            res[curr] = deck[counter]
11            counter += 1
12            if queue:
13                queue.append(queue.popleft())
14        return res
15