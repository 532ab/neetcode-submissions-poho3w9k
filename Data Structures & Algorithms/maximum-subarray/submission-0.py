class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = 0

        for i in nums:
            curr = max(curr, 0)
            curr += i
            max_sum = max(max_sum, curr)
        
        return max_sum