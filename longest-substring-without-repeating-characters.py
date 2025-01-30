class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxSoFar = 0
        track = set()
        while right < len(s):
            curr = s[right]
            if curr in track:
                track.remove(s[left])
                left += 1
                continue
            count = right - left + 1
            maxSoFar = max(maxSoFar, count)
            track.add(s[right])
            right += 1
        return maxSoFar