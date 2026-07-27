from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # Map to track target character counts
        t_count = Counter(t)
        required = len(t_count)  # Number of unique characters needed
        
        # Map to track counts in the current window
        window_count = {}
        formed = 0  # Unique characters satisfying target counts
        
        # Track best window: (window_length, left_index, right_index)
        ans = (float("inf"), 0, 0)
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Increment formed if char requirement is satisfied
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Contract window from the left while all characters are matched
            while left <= right and formed == required:
                # Update optimal window size
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Pop the leftmost character out of the window
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                
                left += 1
                
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]