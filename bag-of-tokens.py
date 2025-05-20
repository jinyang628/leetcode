class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        res = max_res = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                res += 1
                if res > max_res:
                    max_res = res
            elif res > 0:
                res -= 1
                power += tokens[right]
                right -= 1
            else:
                break
        return max_res