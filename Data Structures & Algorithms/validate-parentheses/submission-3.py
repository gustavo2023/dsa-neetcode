class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        parentheses_map = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in parentheses_map:
                if len(stack) != 0:
                    if parentheses_map[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0