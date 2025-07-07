class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        right = math.ceil(num // 2)
        left = 1 
        while left <= right:
            mid = left + (right - left) // 2
            curr = mid ** 2
            if curr == num:
                return True
            elif curr < num:
                left = mid + 1
            else:
                right = mid - 1
        return False