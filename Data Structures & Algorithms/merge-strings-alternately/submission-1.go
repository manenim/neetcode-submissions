func mergeAlternately(word1 string, word2 string) string {
	w1Rune := []rune(word1)
	w2Rune := []rune(word2)
	result := ""

	fmt.Println(w1Rune, w2Rune)

	for i := range max(len(w1Rune), len(w2Rune)) {
		if i < len(w1Rune) {
			result += string(w1Rune[i])
		}
		if i < len(w2Rune) {
			result += string(w2Rune[i])
		}
	}

	return result

}
