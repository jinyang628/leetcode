class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        wish = self.countAndSay(n - 1)
        pointer = counter = 0
        curr = wish[pointer]
        res = []
        while pointer < len(wish):
            if wish[pointer] == curr:
                counter += 1
            else:
                res.append(str(counter))
                res.append(curr)
                curr = wish[pointer]
                counter = 1
            pointer += 1
        res.append(str(counter))
        res.append(curr)
        return "".join(res)