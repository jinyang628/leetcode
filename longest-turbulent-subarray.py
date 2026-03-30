class Solution {
    public int maxTurbulenceSize(int[] A) {
        if (A == null) return 0;
        if (A.length == 1) return 1;
        boolean inc = A[0] < A[1];
        int count = (A[0] != A[1]) ? 2 : 1;
        int max = count;
        for (int j = 2; j < A.length; ++j) {
            if (inc && A[j-1] > A[j] || !inc && A[j-1] < A[j]) {
                count++;
            }
            else {
                count = (A[j-1] != A[j]) ? 2 : 1;
            }
            inc = A[j-1] < A[j];
            max = Math.max(max, count);
        } 
        return max;
    }
}