class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        first = {}
        second = {}
        
        for i in range(len(s)):
            first[s[i]] = 1 + first.get(s[i], 0)
        
        for i in range(len(t)):
            second[t[i]] = 1 + second.get(t[i], 0)
        
        return first == second
