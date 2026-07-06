class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # Move the left pointer right if it's not an alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
            
            # Move the right pointer left if it's not an alphanumeric character
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Compare characters case-insensitively
            if s[l].lower() != s[r].lower():
                return False
            
            # Move both pointers inward
            l += 1
            r -= 1
            
        return True