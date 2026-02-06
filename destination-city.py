1class Solution:
2    def destCity(self, paths: List[List[str]]) -> str:
3        cities = set()
4        outbound = defaultdict(list)
5        for a, b in paths:
6            cities.add(a)
7            cities.add(b)
8            outbound[a].append(b)
910        for city in cities:
11            if not outbound[city]:
12                return city