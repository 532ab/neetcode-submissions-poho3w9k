class Solution:
    def isValid(self, s: str) -> bool:
        # Map CLOSING brackets to their corresponding OPENING brackets
        store = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in store:
                # Check if stack has an open bracket and if it matches
                if stack and stack[-1] == store[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, push it to the stack
                stack.append(char)
        
        # Valid only if all opened brackets were closed (stack is empty)
        return len(stack) == 0