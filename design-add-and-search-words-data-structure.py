1class Node:
2    def __init__(self, is_end: bool = False):
3        self.children = {} # key is the character, val is a Node
4        self.is_end = is_end
56    def addWord(self, idx: int, word: str) -> None:
7        if idx == len(word):
8            self.is_end = True
9            return
1011        if word[idx] not in self.children:
12            self.children[word[idx]] = Node()
13        self.children[word[idx]].addWord(idx + 1, word)
1415    def search(self, idx: int, word: str) -> bool:
16        if idx == len(word):
17            return self.is_end
1819        res = False
20        if word[idx] == ".":
21            for _, child in self.children.items():
22                res = res or child.search(idx + 1, word)
23        else:
24            for key, child in self.children.items():
25                if key == word[idx]:
26                    return child.search(idx + 1, word)
27        return res
282930class WordDictionary:
3132    def __init__(self):
33        self.node = Node(True)
3435    def addWord(self, word: str) -> None:
36        self.node.addWord(0, word)
3738    def search(self, word: str) -> bool:
39        return self.node.search(0, word)
40414243# Your WordDictionary object will be instantiated and called as such:
44# obj = WordDictionary()
45# obj.addWord(word)
46# param_2 = obj.search(word)