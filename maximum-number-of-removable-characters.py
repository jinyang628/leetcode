class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left, right = 0, len(removable) - 1
        def isSubseq(removeEndIdx: int) -> bool:
            removed_idxes = set(removable[:removeEndIdx])
            s_pointer = p_pointer = 0
            while s_pointer < len(s) and p_pointer < len(p):
                if s_pointer in removed_idxes:
                    s_pointer += 1
                elif s[s_pointer] == p[p_pointer]:
                    s_pointer += 1
                    p_pointer += 1
                else:
                    s_pointer += 1
            return p_pointer == len(p)
        while left <= right:
            mid = left + (right - left) // 2
            if isSubseq(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return left