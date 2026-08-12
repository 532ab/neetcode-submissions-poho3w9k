class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        
        for i in nums:
            if i == 1:
                count += 1
                # Track the highest streak seen so far
                max_count = max(max_count, count)
            else:
                # Reset streak counter when encountering a 0
                count = 0
                
        return max_count
