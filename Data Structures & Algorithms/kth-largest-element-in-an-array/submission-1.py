
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify_max(nums)

        target = k

        while target > 1:

            heapq.heappop_max(nums)
            target -= 1
        
        return heapq.heappop_max(nums)