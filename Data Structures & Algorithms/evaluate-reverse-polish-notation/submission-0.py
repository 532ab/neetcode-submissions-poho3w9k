class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        hold = {'+', "-", "*", "/"}

        res = []

        for i in range(len(tokens)):
            # Check if the current token is an operator
            if tokens[i] in hold:
                # Pop the second operand first, then the first operand
                b = res.pop()
                a = res.pop()
                
                # Perform the operation and append the result back
                if tokens[i] == '+':
                    res.append(a + b)
                elif tokens[i] == '-':
                    res.append(a - b)
                elif tokens[i] == '*':
                    res.append(a * b)
                elif tokens[i] == '/':
                    # Python int() handles the required truncation toward zero
                    res.append(int(a / b))
            else:
                # If it's a number, convert it from string to int and add to res
                res.append(int(tokens[i]))
                
        # The final remaining item in the list is the answer
        return res[0]
