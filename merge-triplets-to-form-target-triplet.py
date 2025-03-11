class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]
        for one, two, three in triplets:
            if one == target[0] and two <= target[1] and three <= target[2]:
                res[0] = True 
            if one <= target[0] and two == target[1] and three <= target[2]:
                res[1] = True
            if one <= target[0] and two <= target[1] and three == target[2]:
                res[2] = True
        return res[0] and res[1] and res[2]