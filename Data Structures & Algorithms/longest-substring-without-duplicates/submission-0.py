class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # If we see a duplicate, shrink the window from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # Add the current character and track the max size
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len