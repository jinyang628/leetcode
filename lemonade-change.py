from collections import Counter
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = Counter()
        for bill in bills:
            print(counter)
            if bill == 5:
                counter[5] += 1
            elif bill == 10:
                if not counter[5]:
                    return False
                counter[5] -= 1
                counter[10] += 1
            elif bill == 20:
                if counter[10] >= 1:
                    if not counter[5]:
                        return False
                    counter[10] -= 1
                    counter[5] -= 1
                else:
                    if counter[5] < 3:
                        return False
                    counter[5] -= 3
                counter[20] += 1
        return True