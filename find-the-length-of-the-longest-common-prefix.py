class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {} # key is val, value is the node
    def add(self, val: str, idx: int):
        if idx == len(val):
            return 
        if val[idx] not in self.children:
            node = TrieNode(val[idx])
            self.children[val[idx]] = node
        self.children[val[idx]].add(val, idx + 1)
    def get_longest_prefix(self, val: str, idx: int, count: int) -> int:
        if idx == len(val):
            return count 
        if val[idx] not in self.children:
            return count 
        node = self.children[val[idx]]
        return node.get_longest_prefix(val, idx + 1, count + 1)
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        node = TrieNode(None)
        for element in arr1:   
            element = str(element)
            node.add(element, 0)
        maxSoFar = 0
        for element in arr2:
            element = str(element)
            maxSoFar = max(
                maxSoFar, node.get_longest_prefix(element,0,0)
            )
        return maxSoFar