func containsNearbyDuplicate(nums []int, k int) bool {

	seen := make(map[int]struct{})

	for i, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		}
		seen[num] = struct{}{}
		if len(seen) > k {
			delete(seen, nums[i - k])
		}
	}
	return false

}
