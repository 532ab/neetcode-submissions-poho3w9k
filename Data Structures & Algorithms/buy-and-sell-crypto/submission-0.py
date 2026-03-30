class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        maxProfit = 0

        for i in range(len(prices)):
            left = prices[i]
            for j in range(i+1, len(prices)):
                    temp = prices[j] - left
                    if(maxProfit < temp):
                        maxProfit = temp
        
        return maxProfit
        




        