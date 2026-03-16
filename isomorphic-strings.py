1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        s_to_t = {}
4        t_to_s = {}
5        for idx, a in enumerate(s):
6            b = t[idx]
7            if a in s_to_t and b in t_to_s:
8                if s_to_t[a] != b:
9                    return False
10                if t_to_s[b] != a:
11                    return False
12            elif a in s_to_t or b in t_to_s:
13                return False
14            else:
15                s_to_t[a] = b
16                t_to_s[b] = a
17        return True