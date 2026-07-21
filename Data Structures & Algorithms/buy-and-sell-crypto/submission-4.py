class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        left = 0
        right = 1
        maxProf = 0

        while left < right and right < len(prices):
            curProf = prices[right] - prices[left]
            if curProf > maxProf:
                maxProf = curProf
            if prices[right] < prices[left]:
                left = right
            right += 1
            
        return maxProf



        

            





        