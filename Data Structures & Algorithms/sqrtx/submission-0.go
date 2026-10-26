func mySqrt(x int) int {
	l, r := 0, x
	best_guess := 0

	for l <= r {
		mid := l + (r-l)/2
		midSquare := mid * mid

		if midSquare == x {
			return mid
		}
		if midSquare > x {
			r = mid - 1
		} else {
			best_guess = mid
			l = mid + 1
		}
	}

	return best_guess

}
