class Solution:
    # O(n) time | O(n) space
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0
        # monostack represents buildings that were built together
        # (height, work to make it)
        monostack = [(0, 0)]
        for h in target:
            work = max(0, h - monostack[-1][0])
            # if current building is larger than previous ones
            # it couldn't have been built all together
            while monostack and h >= monostack[-1][0]:
                _, prev_work = monostack.pop()
                operations += prev_work
            monostack.append((h, work))
        while monostack:
            operations += monostack.pop()[1]
        return operations