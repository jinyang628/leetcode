1class Solution:
2    def countPaths(self, n: int, roads: List[List[int]]) -> int:
3        res = 0
4        MOD = 10 ** 9 + 7
5        minTime = None
6        heap = [(0, 0)] # cost, node
7        neighbors = defaultdict(list) # neighbor, path_cost
8        for u, v, time in roads:
9            neighbors[u].append((v, time))
10            neighbors[v].append((u, time))
11        distances = [float('inf')] * n
12        distances[0] = 0
13        ways = [0] * n
14        ways[0] = 1
15        while heap:
16            cost, node = heapq.heappop(heap)
17            if cost > distances[node]:
18                continue
1920            for neighbor, path_cost in neighbors[node]:
21                new_cost = path_cost + cost
22                if distances[neighbor] < new_cost:
23                    continue
24                elif distances[neighbor] == new_cost:
25                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
26                else:
27                    ways[neighbor] = ways[node]
28                    distances[neighbor] = new_cost
29                    heapq.heappush(heap, (new_cost, neighbor))
30        return ways[n - 1]
31