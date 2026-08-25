class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        if not matrix:
            return False

        left = 0

        right = len(matrix) - 1

        mid = (left + right) // 2

        if right == 0:
            return self.searchHelp(matrix[mid], target)

        while left <= right:
            if not matrix[mid]:
                return False
            elif matrix[mid][-1] < target:
                left = mid + 1
                mid = (left + right) // 2
            elif matrix[mid][0] > target:
                right = mid - 1
                mid = (left + right) // 2
            else:
                break
        return self.searchHelp(matrix[mid], target)

    def searchHelp(self, arr: List[List[int]], tar: int) -> bool:

        left = 0
        right = len(arr) - 1
        mid = (left + right) // 2
        middle = mid
        if tar > arr[-1]:
            return False
        elif tar < arr[0]:
            return False
        while left <= right:
            if tar > arr[mid]:
                left = mid + 1
                mid = (left + right) // 2
            elif tar < arr[mid]:
                right = mid - 1
                mid = (left + right) // 2
            else:
                return True  
          
        return False
                