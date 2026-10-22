func topKFrequent(nums []int, k int) []int {
	seen := make(map[int]int)
	buckets := make([][]int, len(nums)+1)
	for _, num := range nums {
		seen[num]++
	}

	for key, val := range seen {
		buckets[val] = append(buckets[val], key)
	}

	var results []int
	for i := len(buckets)-1; i >= 0; i-- {
		for _, num := range buckets[i] {
			results = append(results, num)
		}

		if len(results) == k {
			return results
		}
	}

	return results 

}
