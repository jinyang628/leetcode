class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1_counter = v2_counter = 0
        def trim_leading_zeros(s: str) -> int:
            lst = []
            for char in s:
                if lst or char != "0":
                    lst.append(char)
            if not lst:
                return 0
            return int("".join(lst))
        while v1_counter < len(v1) and v2_counter < len(v2):
            v1_val = trim_leading_zeros(v1[v1_counter])
            v2_val = trim_leading_zeros(v2[v2_counter])
            if v1_val < v2_val:
                return -1
            elif v1_val > v2_val:
                return 1
            v1_counter += 1
            v2_counter += 1
        while v1_counter < len(v1):
            v1_val = trim_leading_zeros(v1[v1_counter])
            if v1_val != 0:
                return 1
            v1_counter += 1
        while v2_counter < len(v2):
            v2_val = trim_leading_zeros(v2[v2_counter])
            if v2_val != 0:
                return -1
            v2_counter += 1
        return 0