class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            curr = digits[i]
            new = curr + carry
            if new == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = new
                carry = 0
        if carry == 1:
            return [1] + digits
        else:
            return digits