class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        res = []
        count = i = 0
        for j, val in enumerate(s):
            count += 1 if val == "1" else -1
            if not count:
                res.append('1' + self.makeLargestSpecial(s[i+1:j]) + '0')
                i = j + 1
        return "".join(sorted(res)[::-1])