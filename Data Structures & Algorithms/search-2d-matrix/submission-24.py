class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        if not matrix:
            return False

        left = 0

        right = len(matrix) - 1

        mid = (left + right) // 2

        if right == 0:
            return self.searchHelp(matrix[mid], target) == 0

        while left <= right:
            if not matrix[mid]:
                return False
            elif self.searchHelp(matrix[mid], target) > 1:
                return False
            elif self.searchHelp(matrix[mid], target) > 0:
                left = mid + 1
                mid = (left + right) // 2
            elif self.searchHelp(matrix[mid], target) < 0:
                right = mid - 1
                mid = (left + right) // 2
            else:
                return True
        return False

    def searchHelp(self, arr: List[List[int]], tar: int) -> int:

        left = 0
        right = len(arr) - 1
        mid = (left + right) // 2
        middle = mid
        if tar > arr[-1]:
            return 1
        elif tar < arr[0]:
            return -1
        while left <= right:
            if tar > arr[mid]:
                left = mid + 1
                mid = (left + right) // 2
            elif tar < arr[mid]:
                right = mid - 1
                mid = (left + right) // 2
            else:
                return 0   
          
        return 3
                