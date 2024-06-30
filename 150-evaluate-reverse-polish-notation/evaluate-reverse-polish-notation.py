class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = set(["+", "-", "*", "/"])
        for char in tokens:
            if char in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if char == "+":
                    stack.append(operand1 + operand2)
                elif char == "-":
                    stack.append(operand1 - operand2)
                elif char == "*":
                    stack.append(operand1 * operand2)
                else:
                    if operand1 * operand2 > 0 or operand1 % operand2 == 0:
                        stack.append(operand1 // operand2)
                    else:
                        stack.append((operand1 // operand2) + 1)
            else:
                stack.append(int(char))

        return stack.pop()