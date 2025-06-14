class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = right = currWhite = 0
        minSoFar = float('inf')
        while right < len(blocks):
            if blocks[right] == "W":
                currWhite += 1
            right += 1
            if right < k:
                continue
            minSoFar = min(minSoFar, currWhite)
            if blocks[left] == "W":
                currWhite -= 1
            left += 1
        return minSoFar