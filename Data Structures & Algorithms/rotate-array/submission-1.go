func rotate(nums []int, k int) {
	k = k % len(nums)
	reverse(nums, 0, len(nums)-1 )
	reverse(nums, 0, k-1)
	reverse(nums, k, len(nums)-1)
}

func reverse(nums []int, l int, r int) {
	for l <= r {
		nums[l], nums[r] = nums[r], nums[l] 
		l++
		r--
	}
}
