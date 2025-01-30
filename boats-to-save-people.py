class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = res = 0
        right = len(people) - 1
        while left <= right:
            curr = people[left] + people[right]
            if curr <= limit:
                res += 1
                left += 1
                right -= 1
            else:
                res += 1
                right -= 1
        return res