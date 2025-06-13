class Solution {
    public int closedIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int lands = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    lands++;
                }
            }
        }
        UnionFind uf = new UnionFind(m * n, lands);
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                uf.initEdge(i * n);
            }
            if (grid[i][n - 1] == 0) {
                uf.initEdge(i * n + n - 1);
            }
        }
        for (int j = 1; j < n - 1; j++) {
            if (grid[0][j] == 0) {
                uf.initEdge(j);
            }
            if (grid[m - 1][j] == 0) {
                uf.initEdge((m - 1) * n + j);
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    if (i > 0 && grid[i - 1][j] == 0) {
                        uf.union(i * n + j, (i - 1) * n + j);
                    }
                    if (j > 0 && grid[i][j - 1] == 0) {
                        uf.union(i * n + j, i * n + j - 1);
                    }
                }
            }
        }
        return uf.getCount();
    }
    class UnionFind {
        private int[] parent;
        private int[] rank;
        private boolean[] onEdge;
        private int count;
        public UnionFind(int n, int count) {
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
            rank = new int[n];
            onEdge = new boolean[n];
            this.count = count;
        }
        public void initEdge(int x) {
            if (!onEdge[x]) {
                parent[x] = 0;
                onEdge[x] = true;
                count--;
            }
        }
        public void union(int x, int y) {
            int rootx = find(x);
            int rooty = find(y);
            if (rootx != rooty) {
                if (rank[rootx] > rank[rooty]) {
                    parent[rooty] = rootx;
                    onEdge[rootx] |= onEdge[rooty];
                } else if (rank[rootx] < rank[rooty]) {
                    parent[rootx] = rooty;
                    onEdge[rooty] |= onEdge[rootx];
                } else {
                    parent[rooty] = rootx;
                    onEdge[rootx] |= onEdge[rooty];
                    rank[rootx]++;
                }
                count--;
            }
        }
        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        public int getCount() {
            return count;
        }
    }
}