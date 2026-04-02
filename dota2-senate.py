1from collections import deque, Counter
2class Solution:
3    def predictPartyVictory(self, senate: str) -> str:
4        counter = Counter(senate)
5        queue = deque(list(senate))
6        dire_banned = radiant_banned = 0
7        while queue:
8            curr = queue.popleft()
9            if curr == "R":
10                if radiant_banned:
11                    radiant_banned -= 1
12                    counter["R"] -= 1
13                else:
14                    if not counter["D"]:
15                        return "Radiant"
16                    else:
17                        dire_banned += 1
18                        queue.append("R")
19            else:
20                if dire_banned:
21                    dire_banned -= 1
22                    counter["D"] -= 1
23                else:
24                    if not counter["R"]:
25                        return "Dire"
26                    else:
27                        radiant_banned += 1
28                        queue.append("D")