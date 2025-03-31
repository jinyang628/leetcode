class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            prev = res[-1]
            new = [1]
            for i in range(len(prev) - 1):
                new.append(prev[i] + prev[i + 1])
            new.append(1)
            res.append(new)
        return res