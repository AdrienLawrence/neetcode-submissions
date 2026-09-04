import math
import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]

        result = [[]]

        for num in nums:

            new_result = []

            for sub in result:
                for i in range(len(sub) + 1):
                    temp = copy.deepcopy(sub)
                    temp.insert(i, num)
                    new_result.append(temp)

            result = copy.deepcopy(new_result)
                    


        return result