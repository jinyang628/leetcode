1from collections import defaultdict
2import heapq
3from typing import List
45class Solution:
6    def minimumCost(
7        self,
8        source: str,
9        target: str,
10        original: List[str],
11        changed: List[str],
12        cost: List[int],
13    ) -> int:
14        neighbors = defaultdict(list)
15        for i in range(len(original)):
16            neighbors[original[i]].append((changed[i], cost[i]))
1718        cost_tracker = defaultdict(dict)
19        total = 0
2021        for i, char in enumerate(source):
22            tgt = target[i]
2324            if char == tgt:
25                continue
2627            if tgt in cost_tracker[char]:
28                total += cost_tracker[char][tgt]
29                continue
3031            heap = [(0, char)]
32            visited = set()
33            found = False
3435            while heap:
36                curr_cost, curr = heapq.heappop(heap)
37                if curr in visited:
38                    continue
39                visited.add(curr)
4041                if curr == tgt:
42                    cost_tracker[char][tgt] = curr_cost
43                    total += curr_cost
44                    found = True
45                    break
4647                for nxt, w in neighbors[curr]:
48                    if nxt not in visited:
49                        heapq.heappush(heap, (curr_cost + w, nxt))
5051            if not found:
52                return -1
5354        return total
55