class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Key is now OPENING, Value is CLOSING
        openToClose = { "(": ")", "[": "]", "{": "}" }
        
        for c in s:
            if c in openToClose:
                # 1. If it's an opening bracket, push it to the stack
                stack.append(c)
            else:
                # 2. If it's a closing bracket, check for a match
                if not stack or openToClose[stack[-1]] != c:
                    return False
                stack.pop() # It matched, so remove the opening bracket
                
        return not stack