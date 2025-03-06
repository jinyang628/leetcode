class Solution:
    def isHappy(self, n: int) -> bool:
        track = set() # tracks the values seen so far
        while n != 1:
            if n in track:
                return False
            track.add(n)
            new_num = 0
            for c in str(n):
                new_num += int(c) ** 2
            n = new_num
        return True