class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0

        right = len(heights) - 1

        max_h = (right - left)*(min(heights[left], heights[right]))

        while left < right:
            cur_h = (right - left)*(min(heights[left], heights[right]))

            if cur_h > max_h:
                max_h = cur_h
            
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
        return max_h