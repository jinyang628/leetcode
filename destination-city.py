class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        track = {}
        cities = set()
        for src, dst in paths:
            cities.add(src)
            cities.add(dst)
            track[src] = dst        
        for city in cities:
            if city not in track:
                return city