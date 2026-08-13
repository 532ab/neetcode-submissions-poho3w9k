class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i] not in ["+", "D", "C"]:
                stack.append(int(operations[i]))
            elif operations[i] == "+":
                total = stack[-1] + stack[-2]
                stack.append(total)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                new_score = 2 * stack[-1]
                stack.append(new_score)

        return sum(stack)