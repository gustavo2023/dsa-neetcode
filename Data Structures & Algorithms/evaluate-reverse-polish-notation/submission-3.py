class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 1:
            return int(tokens[-1])
        
        stack = []
        operands = ["+", "-", "*", "/"]

        for i in range(len(tokens)):
            if tokens[i] in operands:
                second_digit = int(stack.pop())
                first_digit = int(stack.pop())
                
                if tokens[i] == "+":
                    stack.append(first_digit + second_digit)
                elif tokens[i] == "-":
                    stack.append(first_digit - second_digit)
                elif tokens[i] == "*":
                    stack.append(first_digit * second_digit)
                else:
                    stack.append(int(first_digit / second_digit))
            else:
                stack.append(tokens[i])
        
        return stack[-1]