class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        maxS = 1

        nums = set(nums)

        for x in nums:
            if (x-1) in nums:
                continue
            tempS = 1
            while True:
                if (x + tempS) in nums:
                    tempS += 1
                    if tempS > maxS:
                        maxS = tempS
                else:
                    break
        return maxS


