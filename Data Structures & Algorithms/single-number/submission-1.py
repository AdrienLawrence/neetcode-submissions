class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for i, num in enumerate(nums):
            if num not in nums[i + 1: len(nums)] and num not in nums[0:i]:
                return num