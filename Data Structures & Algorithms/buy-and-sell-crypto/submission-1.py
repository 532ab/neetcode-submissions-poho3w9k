class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr_profit = prices[j] - prices[i]

                if curr_profit > max_profit:
                    max_profit = curr_profit
        return max_profit