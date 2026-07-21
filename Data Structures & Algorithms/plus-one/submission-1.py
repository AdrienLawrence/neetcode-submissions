class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.reverse()
        solved = []
        carry = 0

        for i, num in enumerate(digits):
            if i == 0:
                if num == 9:
                    solved.append(0)
                    carry = 1
                else:
                    solved.append(num + 1)
            else:
                if carry == 1:
                    if num + carry > 9:
                        solved.append((num + carry) % 10)
                    else:
                        solved.append(num + carry)
                        carry = 0
                else:
                    solved.append(num)
        if carry == 1:
            solved.append(1)
            
        solved.reverse()            
        return solved