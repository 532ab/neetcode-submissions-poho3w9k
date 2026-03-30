class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        first_string = {}
        second_string = {}

        for i in range(len(s)):
            first_string[s[i]] = 1 + first_string.get(s[i],0)
            second_string[t[i]] = 1 + second_string.get(t[i],0)
        return first_string == second_string