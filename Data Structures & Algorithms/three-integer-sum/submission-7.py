class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = [] 
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet not in result:
                        result.append(triplet)
                    left += 1
                    right -=1
        return result
