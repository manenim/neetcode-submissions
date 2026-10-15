func containsNearbyDuplicate(nums []int, k int) bool {
	// Initialize our sliding window HashSet using the zero-byte struct trick
	window := make(map[int]struct{})

	for i, num := range nums {
		// 1. Check: If 'num' is already in our window, we found a duplicate within k distance!
		if _, ok := window[num]; ok {
			return true
		}

		// 2. Add: Put the current number into the window
		window[num] = struct{}{}

		// 3. Evict: If our window exceeds size k, remove the oldest element that fell out of range
		if len(window) > k {
			delete(window, nums[i-k])
		}
	}

	return false
}
