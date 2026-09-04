import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        result = [[]]

        for num in nums:
            temp = copy.deepcopy(result)

            for i in range(0, len(result)):
                result[i].append(num)

            for sub in temp:
                result.append(sub)

        return result
        

            