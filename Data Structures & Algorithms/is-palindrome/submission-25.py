class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t = s.lower()
        left = 0
        right = len(s) - 1
        check = False

        for char in s:
            if char.isalnum() == True:
                while left < right:
                    while t[left].isalnum() == False:
                        left += 1
                    while t[right].isalnum() == False:
                        right -= 1
                    if t[left] != t[right]:
                        return False
                    left += 1
                    right -= 1
                break
        
        return True