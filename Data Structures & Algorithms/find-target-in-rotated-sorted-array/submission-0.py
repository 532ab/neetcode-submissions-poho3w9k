class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = left + ((right - left) // 2)
            
            # 1. Found the target!
            if nums[middle] == target:
                return middle
            
            # 2. Check if the LEFT half is normally sorted
            if nums[left] <= nums[middle]:
                # Is the target inside this sorted left half?
                if nums[left] <= target < nums[middle]:
                    right = middle - 1  # Search left
                else:
                    left = middle + 1   # Search right
                    
            # 3. Otherwise, the RIGHT half must be normally sorted
            else:
                # Is the target inside this sorted right half?
                if nums[middle] < target <= nums[right]:
                    left = middle + 1   # Search right
                else:
                    right = middle - 1  # Search left
                    
        return -1