import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        sorted_points = sorted(points, key=lambda point: math.sqrt(point[0]**2 + point[1]**2))

        result = []

        for i in range(k):
            result.append(sorted_points[i])


        return result