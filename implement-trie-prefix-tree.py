1class Trie(object):
23    def __init__(self):
4        self.is_end = False
5        self.children = {}
67    def insert(self, word):
8        """
91011        """
12        if not word:
13            self.is_end = True
14            return
15        if word[0] not in self.children:
16            self.children[word[0]] = Trie()
17        self.children[word[0]].insert(word[1:])
18192021    def search(self, word):
22        """
232425        """
26        if not word:
27            return self.is_end
28        if word[0] not in self.children:
29            return False
30        return self.children[word[0]].search(word[1:])
313233    def startsWith(self, prefix):
34        """
353637        """
38        if not prefix:
39            return True
40        if prefix[0] not in self.children:
41            return False
42        return self.children[prefix[0]].startsWith(prefix[1:])
43444546# Your Trie object will be instantiated and called as such:
47# obj = Trie()
48# obj.insert(word)
49# param_2 = obj.search(word)
50# param_3 = obj.startsWith(prefix)