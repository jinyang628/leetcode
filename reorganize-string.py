1import heapq
2class Solution:
3    def reorganizeString(self, s: str) -> str:
4        heap = []
5        counter = Counter(s)
6        res = []
7        cooldown = []
8        for key, freq in counter.items():
9            heapq.heappush(heap, (-freq, key))
1011        while heap:
12            print(heap, cooldown)
13            negative_freq, key = heapq.heappop(heap)
14            if res and res[-1] == key:
15                cooldown = [(negative_freq, key)]
16                continue
17            negative_freq += 1
18            res.append(key)
19            if negative_freq:
20                heapq.heappush(heap, (negative_freq, key))
21            if cooldown:
22                heapq.heappush(heap, (cooldown[0][0], cooldown[0][1]))
23                cooldown = []
24        if cooldown:
25            return ""
26        return "".join(res)
2728