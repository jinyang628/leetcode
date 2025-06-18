class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        arr1 = []
        arr2 = []
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue 
            arr1.append(s1[i])
            arr2.append(s2[i])
        if len(arr1) > 2:
            return False
        elif not len(arr1):
            return True
        elif len(arr1) == 1:
            if arr1[0] == arr2[0]:
                return True
            return False
        return arr1[0] == arr2[1] and arr1[1] == arr2[0]