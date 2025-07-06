class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = right = avg = res = 0 
        while right <= len(arr):
            if avg >= threshold and (right - left) == k:
                print(left, right)
                res += 1
            if right >= len(arr):
                break
            avg += arr[right]/k
            if right < k:
                right += 1
                continue
            avg -= arr[left]/k
            left += 1
            right += 1
        return res