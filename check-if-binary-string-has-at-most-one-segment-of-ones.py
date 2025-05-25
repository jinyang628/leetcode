class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        can_be_one = None
        for char in s:
            if char == "0":
                if can_be_one:
                    can_be_one = False
                continue
            if can_be_one is False:
                return False
            can_be_one = True
        return True