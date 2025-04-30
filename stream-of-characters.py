from collections import deque
class TrieNode:
    def __init__(self, val: str, is_end: bool = False):
        self.val = val
        self.children = {}
        self.is_end = is_end 
    def add(self, word: str):
        if not word:
            self.is_end = True
            return 
        if word[0] in self.children:
            self.children[word[0]].add(word[1:])
        else:
            new_child = TrieNode(word[0])
            new_child.add(word[1:])
            self.children[word[0]] = new_child
    def isPresent(self, word: str) -> bool:
        if self.is_end:
            return True
        if not word:
            return False
        if word[0] not in self.children:
            return False
        return self.children[word[0]].isPresent(word[1:])
class StreamChecker:
    def __init__(self, words: List[str]):
        node = TrieNode("")
        for word in words:
            node.add(word[::-1])  
        self.node = node      
        self.stream = deque([])
        self.max_len = max(len(w) for w in words)
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.max_len:
            self.stream.popleft()
        return self.node.isPresent(list(self.stream)[::-1])
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)