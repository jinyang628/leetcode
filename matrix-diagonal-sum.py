public int diagonalSum(int[][] mat) {
    int n = mat.length;
    return IntStream.range(0, n)
            .map(i -> mat[i][i] + mat[i][n-1-i])
            .sum() - (n % 2 == 1 ? mat[n/2][n/2] : 0);
}