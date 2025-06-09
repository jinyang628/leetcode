class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        while True:
            curr = None
            for element in strs:
                if count >= len(element):
                    return strs[0][:count]
                if curr == None:
                    curr = element[count]
                elif curr != element[count]:
                    return strs[0][:count]
            count += 1
        return strs[0][:count]