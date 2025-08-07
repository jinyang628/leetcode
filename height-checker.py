func heightChecker(heights []int) int {
	n := len(heights)
	hCount := make([]int, 101)
    for i := 0; i < n; i++ {
        hCount[heights[i]]++
    }
	count := 0
    j := 0
	for i := 1; i <= 100; i++ {
        for hCount[i] > 0 {
            if heights[j] != i {
                count++
            }
            j++
            hCount[i]--
        }
	}
	return count
}