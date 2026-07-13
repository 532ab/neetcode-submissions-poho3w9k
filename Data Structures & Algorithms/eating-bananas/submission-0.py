import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            mid_speed = (left + right) // 2
            
            # Clean Python shortcut to sum up all the hours
            total_hours = sum(math.ceil(pile / mid_speed) for pile in piles)
            
            if total_hours <= h:
                right = mid_speed - 1  # Try to find a smaller speed
            else:
                left = mid_speed + 1   # Must speed up
                
        return left  # Left naturally points to the minimum valid speed
