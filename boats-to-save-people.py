class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = left = 0
        right = len(people) - 1
        people.sort()
        while left <= right:
            if left == right:
                res += 1
                left += 1
                continue
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                res += 1
            else:
                res += 1
                right -= 1
        return res