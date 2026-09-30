func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)
	for idx, num := range nums {
		compliment := target - num
		if _, ok := seen[compliment]; ok {
			return []int{seen[compliment], idx}
		}
		seen[num] = idx
	}
    return []int{}
}
