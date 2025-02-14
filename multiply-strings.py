class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sum = 0
        multiplier_one = 1
        for i in range(len(num2) - 1, -1, -1):
            multiplier_two = 1
            for j in range(len(num1) - 1, -1, -1):
                sum += multiplier_one * multiplier_two * int(num2[i]) * int(num1[j])
                multiplier_two *= 10
            multiplier_one *= 10
        return str(sum)