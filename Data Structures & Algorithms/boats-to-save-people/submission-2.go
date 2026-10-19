func numRescueBoats(people []int, limit int) int {
	sort.Ints(people)
	counter := 0
	l, r := 0, len(people) - 1

	for l <= r {
		weights := people[l] + people[r]
		if weights <= limit {
			l++
			r--
		}else {
			r--
		}
		counter++
	}
	return counter

}
