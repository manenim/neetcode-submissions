func validPalindrome(s string) bool {
	
	l, r := 0, len(s) -1
	for l < r {
		if s[l] != s[r] {
			return isValidPalindrome(s, l+1, r) || isValidPalindrome(s, l, r-1)
		}
		l++
		r--
	}
	return true

}

func isValidPalindrome(s string, start, end int) bool {
	for start < end {
		if s[start] != s[end] {
			return false
		}
		start++
		end--
	}
	return true
}
