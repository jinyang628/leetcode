1class Solution:
2    def restoreIpAddresses(self, s: str) -> List[str]:
3        res = []
4        def backtrack(idx: int, curr: str, subset: list[str]) -> None:
5            print(idx, curr, subset)
6            if len(subset) == 4:
7                if idx == len(s):
8                    res.append(".".join(subset))
9                return
1011            while idx < len(s):
12                curr += s[idx]
13                if len(curr) > 1 and curr[0] == "0":
14                    return
15                if int(curr) > 255:
16                    return
17                idx += 1
18                subset.append(curr)
19                backtrack(idx, "", subset)
20                subset.pop()
212223        backtrack(0, "", [])
24        return res
2526