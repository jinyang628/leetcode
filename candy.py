class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        i = 1
        total_candies = len(ratings)
        while i < n:
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue
            current_peak = 0
            while i < n and ratings[i] > ratings[i - 1]:
                current_peak += 1
                total_candies += current_peak
                i += 1
            if i == n:
                return total_candies
            current_valley = 0
            while i < n and ratings[i] < ratings[i - 1]:
                current_valley += 1
                total_candies += current_valley
                i += 1
            total_candies -= min(current_valley, current_peak)
        return total_candies