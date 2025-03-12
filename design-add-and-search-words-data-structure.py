class WordDictionary:
    is_end: bool
    children: dict[str, "WordDictionary"]
    def __init__(self):
        self.is_end = False
        self.children = {}
    def addWord(self, word: str) -> None:
        if not word:
            self.is_end = True
            return
        if word[0] in self.children:
            return self.children[word[0]].addWord(word[1:])
        self.children[word[0]] = WordDictionary()
        self.children[word[0]].addWord(word[1:])
    def search(self, word: str) -> bool:
        if not word:
            return self.is_end
        if word[0] != ".":
            if word[0] in self.children:
                return self.children[word[0]].search(word[1:])
        else:
            res = False
            for k, v in self.children.items():
                res = res or v.search(word[1:])
            return res
        return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)