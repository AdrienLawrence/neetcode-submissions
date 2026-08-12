class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2 or len(s)%2 != 0:
            return False
        
        stack = []

        matches = {")": "(", "]": "[", "}": "{",}

        for char in s:
            if char in matches:
                if stack and stack[-1] == matches.get(char):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
