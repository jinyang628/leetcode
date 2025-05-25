from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        track = defaultdict(list)
        for w, l in matches:
            if not track[w]:        
                track[w] = [1, 0]
            else:
                track[w][0] += 1
            if not track[l]:
                track[l] = [0, 1]
            else:
                track[l][1] += 1
        never_lost = []
        lost_one = []
        for player, matches in track.items():
            if not matches[1]:
                never_lost.append(player)
            elif matches[1] == 1:
                lost_one.append(player)
        never_lost.sort()
        lost_one.sort()
        return [never_lost, lost_one]