class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4:
            return True
        return False