class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_prod = 1
        right_prod = 1
        sums = []
        for num in nums:
            sums.append(left_prod)
            left_prod *= num
           

        for i in range(len(nums) - 1, -1, -1):
            sums[i] = (sums[i]*right_prod)
            right_prod *= nums[i]

        return sums