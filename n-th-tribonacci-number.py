class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0
        first = 0
        second = 1
        third = 1
        curr = 2
        while curr < n:
            new = first + second + third
            first = second
            second = third
            third = new
            curr += 1
        return third