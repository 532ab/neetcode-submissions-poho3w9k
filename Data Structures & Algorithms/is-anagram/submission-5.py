class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_char1 = {}
        count_char2 = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            count_char1[char] = 1 + count_char1.get(char, 0)
        for char in t:
            count_char2[char] = 1 + count_char2.get(char, 0)
        
        return count_char1 == count_char2
        

     
