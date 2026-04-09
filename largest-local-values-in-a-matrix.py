class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(1,len(grid)-1):
            tmp=[]
            for j in range(1,len(grid[0])-1):
                tmp.append(max(grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1]
                              ,grid[i][j-1],grid[i][j],grid[i][j+1]
                              ,grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]))
            ans.append(tmp)
        return ans