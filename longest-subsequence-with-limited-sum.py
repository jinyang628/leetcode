class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefixSums = []
        curr = 0
        for num in nums:
            curr += num
            prefixSums.append(curr)
        ans = []
        for ceiling in queries:
            left, right = 0, len(prefixSums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if prefixSums[mid] > ceiling:
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(left)
        return ans