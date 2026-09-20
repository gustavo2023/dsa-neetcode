class Solution:
    def evalRPN(self, tokens: List[str]) -> int:       
        stack = []
        operands = ["+", "-", "*", "/"]

        for i in range(len(tokens)):
            if tokens[i] in operands:
                second_digit = stack.pop()
                first_digit = stack.pop()
                
                if tokens[i] == "+":
                    stack.append(first_digit + second_digit)
                elif tokens[i] == "-":
                    stack.append(first_digit - second_digit)
                elif tokens[i] == "*":
                    stack.append(first_digit * second_digit)
                else:
                    stack.append(int(first_digit / second_digit))
            else:
                stack.append(int(tokens[i]))
        
        return int(stack[-1])