class StockSpanner {
    // Stack to store pairs of [price, span]
    private Stack<int[]> st;
    public StockSpanner() {
        st = new Stack<>();
    }
    public int next(int price) {
        int cnt = 1; // Span starts at 1 (current day)
        // Pop all prices from stack that are less than or equal to current price
        while (!st.isEmpty() && price >= st.peek()[0]){
            // Add their span to current span
            cnt += st.pop()[1];
        }
        // Push the current price and its total span onto the stack
        st.push(new int[]{price, cnt});
        // Return the span for current price
        return cnt;
    }
}