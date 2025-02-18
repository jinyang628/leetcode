from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1:
            return [1]
        res = []
        track = defaultdict(set) # key is the character, value is a set containing all the idxes it is present at
        for i in range(len(s)):
            curr = s[i]
            track[curr].add(i)
        track[s[0]].remove(0)
        members = set()
        if track[s[0]]:
            members.add(s[0])
        count = 1
        for i in range(1, len(s)):
            if not members:
                res.append(count)
                count = 0
            count += 1
            curr = s[i]
            if curr in members:
                track[curr].remove(i)
                if not track[curr]:
                    members.remove(curr)
            else:
                track[curr].remove(i)
                if track[curr]:
                    members.add(curr)
        res.append(count)
        return res