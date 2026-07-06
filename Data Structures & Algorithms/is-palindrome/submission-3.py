class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue  # Skip the rest of the loop and start over from the top!
                
            if not s[r].isalnum():
                r -= 1
                continue  # Skip the rest of the loop and start over from the top!
            
            # This line is ONLY reached if BOTH l and r are alphanumeric
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True