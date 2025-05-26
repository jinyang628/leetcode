class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res =[]
        for spell in spells:
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if potions[mid] * spell >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(len(potions) - left)
        return res