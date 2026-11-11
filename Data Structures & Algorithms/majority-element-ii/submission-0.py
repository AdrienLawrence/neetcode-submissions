class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        numsD = {}

        new = []

        for num in nums:

            if num in numsD:
                numsD[num] += 1
            else:
                numsD[num] = 1
        
        for num in numsD:

            if numsD[num] > (len(nums) / 3):
                new.append(num)

        return new