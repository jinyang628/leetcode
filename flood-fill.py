class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:   
        row, col = len(image), len(image[0])
        visited = set()
        def dfs(r: int, c: int, original: int) -> None:
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            if (r, c) in visited:
                return
            visited.add((r,c))
            if image[r][c] != original:
                return
            image[r][c] = color
            dfs(r - 1, c, original)
            dfs(r + 1, c, original)
            dfs(r, c - 1, original)
            dfs(r, c + 1, original)
        dfs(sr, sc, image[sr][sc])
        return image