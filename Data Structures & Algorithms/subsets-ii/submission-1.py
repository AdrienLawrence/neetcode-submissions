class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        subsets = [[]]
        
        # For each element in nums
        for i in range(size):
            # Get all current subsets
            current_subsets = subsets[:]
            # Add nums[i] to each existing subset
            for subset in current_subsets:
                new_subset = subset + [nums[i]]
                if new_subset not in subsets:
                    subsets.append(new_subset)
        
        return subsets