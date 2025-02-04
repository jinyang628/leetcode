from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    def backtrack(path: list[int], idx: int):
        print(path)
        print(idx)
        if idx == len(nums):
            res.append(path[:])
            return
        
        path.append(nums[idx])
        idx += 1
        backtrack(path, idx)
        path.pop()
        while idx < len(nums):
            if nums[idx] != nums[idx - 1]:
                break
            idx += 1
        backtrack(path, idx)

    backtrack([], 0)
    return res

print(subsetsWithDup([1,2,2]))