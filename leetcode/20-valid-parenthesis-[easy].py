class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            if len(stack) == 0:
                return False
            if char == ")":
                if stack.pop() != "(":
                    return False
            elif char == "}":
                if stack.pop() != "{":
                    return False
            elif char == "]":
                if stack.pop() != "[":
                    return False
        return len(stack) == 0
