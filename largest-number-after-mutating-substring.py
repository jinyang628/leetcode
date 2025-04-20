class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res = []
        # Tri state
        # 1 -> no mutation attempted yet
        # 2 -> mutation stopped, do not mutate anymore
        # 3 -> continue mutating as much as possible
        canMutate = 1
        for char in num:
            idx = int(char)
            if change[idx] > idx and (canMutate == 1 or canMutate == 3):
                canMutate = 3
                res.append(str(change[idx]))
            elif change[idx] == idx:
                res.append(char)
            else:
                if canMutate == 3:
                    canMutate = 2
                res.append(char)
        return "".join(res)