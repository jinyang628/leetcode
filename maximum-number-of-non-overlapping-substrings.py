class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        idx_track = {}
        start_idx_to_char = {}
        for i in range(len(s)):
            if s[i] not in idx_track:
                idx_track[s[i]] = (i, i)
                start_idx_to_char[i] = s[i]
            else:
                idx_track[s[i]] = (idx_track[s[i]][0], i)
        intervals = []
        for i in range(len(s)):
            _, curr_end = idx_track[s[i]]
            for j in range(i, len(s)):
                required_start, _ = idx_track[s[j]]
                if required_start < i:
                    break
                if j == curr_end:
                    intervals.append([i, j])
                    break
                elif j in start_idx_to_char:
                    curr_end = max(
                        curr_end,
                        idx_track[start_idx_to_char[j]][1]
                    )
        intervals.sort(key=lambda x: x[1])
        final_intervals = []
        for interval in intervals:
            if not final_intervals:
                final_intervals.append(interval)
            else:
                if interval[0] > final_intervals[-1][1]:
                    final_intervals.append(interval)
        for i in range(len(final_intervals)):
            start, end = final_intervals[i]
            final_intervals[i] = s[start: end + 1]
        return final_intervals