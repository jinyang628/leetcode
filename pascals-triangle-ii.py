1class Solution:
2    def getRow(self, rowIndex: int) -> List[int]:
3        if rowIndex == 0:
4            return [1]
5        elif rowIndex == 1:
6            return [1, 1]
7        res = [[1], [1, 1]]
8        for i in range(2, rowIndex + 1):
9            subarr = [1]
10            previous = res[i - 1]
11            for i in range(len(previous) - 1):
12                subarr.append(previous[i] + previous[i + 1])
13            subarr.append(1)
14            res.append(subarr)
15        return res[-1]