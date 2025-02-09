from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        track = Counter(hand)
        unique = sorted(list(set(hand)))  
        for num in unique:
            if num not in track:
                continue
            curr = num
            sizeSoFar = 0
            candidatesToDelete = track[curr]
            while curr in track and groupSize != sizeSoFar:
                sizeSoFar += 1
                track[curr] -= candidatesToDelete
                if not track[curr]:
                    del track[curr]
                curr += 1
            if sizeSoFar != groupSize:
                return False
            sizeSoFar = 0    
        return True