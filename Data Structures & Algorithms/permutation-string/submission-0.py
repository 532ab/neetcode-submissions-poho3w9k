from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_count = Counter(s1)  # The exact "recipe" we are looking for
        
        # Look at every possible chunk in s2 that is the same length as s1
        for i in range(len(s2) - window_size + 1):
            # Take a slice of s2 of length window_size
            current_window = s2[i : i + window_size]
            
            # Count the characters in this slice and compare directly
            if Counter(current_window) == s1_count:
                return True
                
        return False
