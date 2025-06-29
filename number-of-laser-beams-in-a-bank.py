class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        cols = []
        for row in bank:
            count = 0
            for char in row:
                if char == "1":
                    count += 1
            if count:
                cols.append(count)
        for i in range(len(cols) - 1):
            res += cols[i] * cols[i + 1]
        return res