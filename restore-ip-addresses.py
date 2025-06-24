class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start: int, path: list[str]) -> None:
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            for length in range(1, 4):
                if (start + length) > len(s):
                    return 
                segment = s[start: start + length]
                if segment[0] == "0" and len(segment) > 1:
                    return 
                if 0 <= int(segment) <= 255:
                    path.append(str(segment))
                    backtrack(start+length, path)
                    path.pop()
        backtrack(0, [])
        return res