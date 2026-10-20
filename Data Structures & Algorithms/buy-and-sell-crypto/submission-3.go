func maxProfit(prices []int) int {
	minimum := prices[0]
	maxProfit := 0

	for _, price := range prices{
		profit := price - minimum
		maxProfit = max(profit, maxProfit)

		minimum = min(price, minimum)
	}
	return maxProfit
}
