if(i < 0 || j < 0 || i == grid.length || j == grid[0].length) {
        return false;
    }
    if(grid[i][j] == 1) {
        return true;
    }
    grid[i][j] = 1;
    boolean a = countIslands(i+1, j, grid) ;
    boolean b = countIslands(i-1, j, grid) ;
    boolean c = countIslands(i, j+1, grid) ;
    boolean d = countIslands(i, j-1, grid);
    return a && b && c && d;
}`