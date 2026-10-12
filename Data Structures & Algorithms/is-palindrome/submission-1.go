func isPalindrome(s string) bool {
	runes := []rune(s)
	fmt.Println(runes)
	l, r := 0, len(runes) - 1

	for l < r {
		if !IsAlphaNum(runes[l]) {
			l++
			continue
		}
		if !IsAlphaNum(runes[r]){
			r--
			continue
		}
		if strings.ToLower(string(runes[l])) == strings.ToLower(string(runes[r])) {
			l++
			r--
		} else {
			return false
		}

	}
	return true
}

func IsAlphaNum(char rune) bool {
	return unicode.IsLetter(char) || unicode.IsNumber(char)
}