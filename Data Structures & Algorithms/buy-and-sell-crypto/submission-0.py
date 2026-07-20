class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0 # Buy
        ptr = 1 # Sell
        max_profit = 0

        while ptr < len(prices):
            # Case 1: Is today cheaper than our buy day?
            if prices[ptr] < prices[lp]:
                lp = ptr  # Move buy pointer to the new low!
            
            # Case 2: Today is profitable
            else:
                current_profit = prices[ptr] - prices[lp]
                # Keep the biggest profit we've ever seen
                max_profit = max(max_profit, current_profit)
                
            # Right pointer (Time) always moves forward
            ptr += 1
            
        return max_profit