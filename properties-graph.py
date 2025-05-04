class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def find(i: int) -> int:
            res = i
            while res != self.par[res]:
                self.par[res] = self.par[self.par[res]]
                res = self.par[res]
            return res
        def union(a: int, b: int):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return 
            if self.rank[p1] >= self.rank[p2]:
                self.par[p2] = p1 
                self.rank[p1] += self.rank[p2]
            else:
                self.par[p1] = p2
                self.rank[p2] += self.rank[p1]
        length = len(properties)
        self.par = [i for i in range(length)]
        self.rank = [0] * length
        points = [defaultdict(int) for _ in range(length)]
        for i in range(length):
            for num in properties[i]:
                points[i][num] += 1
        for i in range(length):
            for j in range(1, length):
                cmn = sum(1 for num in points[i] if num in points[j])
                if cmn >= k:
                    union(i, j)
        return len(set(find(i) for i in range(length)))