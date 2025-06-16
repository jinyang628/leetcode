from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        for key in sorted_keys:
            freq = count[key]
            if not freq:
                continue
            for i in range(groupSize):
                count[key + i] -= freq
                if count[key + i] < 0:
                    return False
        return True