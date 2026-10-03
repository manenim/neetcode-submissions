func removeElement(nums []int, val int) int {
	r, w := 0, 0

	for r < len(nums) {
		if nums[r] != val {
			nums[w] = nums[r]
			r++
			w++
		}else {
			r++
		}
	}

	return w
    
}
