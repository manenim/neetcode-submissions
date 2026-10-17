func removeDuplicates(nums []int) int {
	l, r := 0, 1
	for r < len(nums) {
		if nums[r] == nums[l] {
			r++
		} else {
			nums[l+1] = nums[r]
			r++
			l++
		}
	}

	return l + 1

}
