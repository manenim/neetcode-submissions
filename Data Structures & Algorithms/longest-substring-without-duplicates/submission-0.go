func lengthOfLongestSubstring(s string) int {
	seen := make(map[rune]int)
	l, r := 0, 0
	max_length := 0

	for idx, char := range s {
		if val, ok := seen[char]; ok {
			l = max(l, val + 1)
		}
		seen[char] = idx
		r++
		max_length = max(max_length, r-l)
	}
	return max_length
}
