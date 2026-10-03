func groupAnagrams(strs []string) [][]string {
	strsMap := make(map[[26]int][]string)
	var result [][]string
	for _, word := range strs {
		var signature [26]int
		for _, char := range word {
		index := char - 'a'
		signature[index]++
		}
		strsMap[signature] = append(strsMap[signature], word)
	}

	for _, val := range strsMap {
		result = append(result, val)
	}
	return result
}
