class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        maxC = 1

        numMax = 0

        freq = {}

        for num in tasks:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key in freq:
            if freq[key] > maxC:
                maxC = freq[key]
                numMax = 1
            elif freq[key] == maxC:
                numMax += 1

        return max(len(tasks), (maxC - 1) * (n + 1) + numMax)