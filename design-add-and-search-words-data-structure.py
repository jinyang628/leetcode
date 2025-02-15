class WordDictionary:
    def __init__(self, val: Optional[str] = None, is_end: bool = False):
        self.val = val
        self.children = {}
        self.is_end = is_end
    def addWord(self, word: str) -> None:
        if not word:
            self.is_end = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = WordDictionary(val=word[0])
        self.children[word[0]].addWord(word[1:])
    def search(self, word: str) -> bool:
        if not word:
            return self.is_end
        if word[0] not in self.children:
            if word[0] != ".":    
                return False
            res = False
            for _, child in self.children.items():
                res = res or child.search(word[1:])
            return res
        return self.children[word[0]].search(word[1:])
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)