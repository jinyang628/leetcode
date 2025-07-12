class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        lines = [set() for _ in range(len(wall))]
        limit = sum(wall[0])
        checking_set = set()
        for i in range(len(wall)):
            count = 0
            for brick in wall[i]:
                count += brick
                if count == limit:
                    continue
                checking_set.add(count)
                lines[i].add(count)
        number_crossed = {}
        for line in checking_set:
            count = 0
            for layer in lines:
                if line in layer:
                    count += 1
            number_crossed[line] = count
        if not number_crossed:
            return len(wall)
        return len(wall) - max(number_crossed.values())