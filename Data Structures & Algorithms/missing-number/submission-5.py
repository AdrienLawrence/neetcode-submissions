class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        actSum = 0
        expSum = 0
        for i, num in enumerate(nums):
            actSum += num
            expSum += i
        expSum += len(nums)
        return expSum - actSum