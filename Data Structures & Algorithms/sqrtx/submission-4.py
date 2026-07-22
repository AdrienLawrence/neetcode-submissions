class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x

        left = 0
        right = x
        mid = x // 2
        while left <= right:
            if mid*mid > x:
                right = mid - 1
                mid = (left + right) // 2
            elif mid*mid < x:
                left = mid + 1
                mid = (left + right) // 2
            else:
                return mid
        return right