func longestCommonPrefix(strs []string) string {
	referenceWord := strs[0]

	for idx := range len(referenceWord) {
		refLetter := referenceWord[idx]
		for i := 1; i < len(strs); i++ {
			currentWord := strs[i]
			if idx >= len(currentWord) || refLetter != currentWord[idx] {
				return referenceWord[:idx]
			}
		}
	}
	return referenceWord
    
}
