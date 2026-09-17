class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_trans = 0
        
        for right in range(1, len(prices)):
            window_diff = prices[right] - prices[left]
            if window_diff > 0:
                max_trans = max(max_trans, window_diff)
            else:
                left = right
        
        return max_trans


        