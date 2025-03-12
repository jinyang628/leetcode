class Trie:
    def __init__(self):
        self.is_end = False
        self.children = {}
    def add_word(self, word: str) -> None:
        if not word:
            self.is_end = True 
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].add_word(word[1:])
    def search_word(self, word: str) -> bool:
        if not word:
            return self.is_end
        if word[0] not in self.children:
            return False
        return self.children[word[0]].search_word(word[1:])
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        for word in words:
            trie.add_word(word)
        row, col = len(board), len(board[0])
        def dfs(r: int, c: int, path: list[str], trie: Trie):
            if trie.is_end:
                trie.is_end = False
                res.append("".join(path[:]))
            if r < 0 or c < 0 or r >= row or c >= col:
                return 
            curr = board[r][c]
            if curr == ".": # already visited
                return
            if curr not in trie.children:
                return
            path.append(curr)
            child_node = trie.children[curr]
            board[r][c] = "."
            dfs(r - 1, c, path, child_node)
            dfs(r + 1, c, path, child_node)
            dfs(r, c - 1, path, child_node)
            dfs(r, c + 1, path, child_node)
            board[r][c] = curr
            path.pop()
        for i in range(row):
            for j in range(col):
                dfs(i, j, [], trie)
        return res