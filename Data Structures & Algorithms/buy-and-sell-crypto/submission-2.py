class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        current_day = prices[0]

        for i in range(1, len(prices)):

            diff = prices[i] - current_day

            max_profit = max(diff, max_profit)

            if diff <= 0:
                current_day = prices[i]
        
        return max_profit