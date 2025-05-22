class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return True
        length = len(arr)
        minimum, maximum = min(arr), max(arr)
        distance = (maximum - minimum)
        if distance % (length - 1):
            return False
        increment = distance // (length - 1)
        members = set(arr)
        for i in range(length):
            curr = minimum + i * increment
            if curr in members:
                continue
            return False
        return True