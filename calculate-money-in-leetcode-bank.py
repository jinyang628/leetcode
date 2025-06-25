class Solution:
    def totalMoney(self, n: int) -> int:
        fullWeeks = n // 7
        spillOver = n % 7
        total = 0
        if fullWeeks:
            first = 1 + 2 + 3 + 4 + 5 + 6 + 7
            last = (7/2) * (fullWeeks + (fullWeeks + 6))
            total += (fullWeeks/2) * (first + last)
        remainder = (spillOver/2) * ((fullWeeks + 1) + (fullWeeks + 1) + (spillOver - 1))
        return int(total + remainder)