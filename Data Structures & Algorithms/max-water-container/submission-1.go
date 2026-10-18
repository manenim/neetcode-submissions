func maxArea(heights []int) int {
	l, r, max_area := 0, len(heights) - 1, 0

	for l < r {
		area := (r - l) * (min(heights[r], heights[l]))
		max_area = max(area, max_area)
		if heights[r] > heights[l] {
			l++
		}else{
			r--
		}

	}
	return max_area
}
