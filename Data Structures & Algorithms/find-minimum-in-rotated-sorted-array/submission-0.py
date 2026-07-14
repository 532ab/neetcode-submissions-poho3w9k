class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # We run the loop while left < right (not <=) because 
        # we want left and right to converge on the single minimum element.
        while left < right:
            middle = left + ((right - left) // 2)

            # If middle is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[middle] > nums[right]:
                left = middle + 1
            # Otherwise, the minimum is in the left half (including middle)
            else:
                right = middle
                
        # When left == right, they both point to the minimum element
        return nums[left]


