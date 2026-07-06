class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Step 1: Sort the array. This is crucial for the two-pointer 
        # approach and makes skipping duplicates incredibly easy.
        nums.sort()
        
        for i in range(len(nums)):
            # Step 2: Skip duplicates for the first element 'i'.
            # If this isn't the first element and it matches the previous element,
            # we skip it to avoid generating duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 3: Initialize the two pointers for the remaining array.
            left = i + 1
            right = len(nums) - 1
            
            # Step 4: Run the two-pointer scan
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    # Sum is too small, move the left pointer right to get a bigger number
                    left += 1
                elif current_sum > 0:
                    # Sum is too big, move the right pointer left to get a smaller number
                    right -= 1
                else:
                    # We found a valid triplet!
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Step 5: Skip duplicates for the 'left' and 'right' pointers.
                    # We look ahead to make sure we don't land on the same numbers again.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward to continue searching within this 'i' loop
                    left += 1
                    right -= 1
                    
        return res