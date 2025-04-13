class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track = {} # key is the number, value is the next greater element
        stack = [] # monotonically decreasing 
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            if not stack:
                track[num] = -1
                stack.append(num)
                continue 
            if stack[-1] > num:
                track[num] = stack[-1]
                stack.append(num)
                continue 
        res = []
        for num in nums1:
            res.append(track[num])
        return res