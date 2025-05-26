class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: (x[0], -x[1]))
        maxSoFar = -1
        for i in range(len(items)):
            _, beauty = items[i]
            maxSoFar = max(maxSoFar, beauty)
            items[i][1] = maxSoFar
        ans = []
        for query in queries:
            if query < items[0][0]:
                ans.append(0)
                continue
            left, right = 0, len(items) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if items[mid][0] > query:
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(items[right][1])
        return ans