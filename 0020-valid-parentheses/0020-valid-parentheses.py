class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        isOpened = {"}":"{", ")":"(", "]":"["}
        for c in s:
            if c in isOpened:
                if stack and stack[-1] == isOpened[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False