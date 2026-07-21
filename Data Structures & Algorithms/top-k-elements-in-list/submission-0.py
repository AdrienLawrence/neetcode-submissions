import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        heap = []
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        for num, count in freqMap.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]