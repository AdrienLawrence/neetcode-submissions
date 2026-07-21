class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            pDict = {")" : "(", "]" : "[", "}" : "{"}
            stack = []
            for i, char in enumerate(s):
                if char in pDict.values():
                    stack.append(char)
                if char in pDict:
                    if stack and stack[-1] == pDict[char]:
                        stack.pop()
                    else:
                        return False
            if not stack:
                return True
         
        return False
            