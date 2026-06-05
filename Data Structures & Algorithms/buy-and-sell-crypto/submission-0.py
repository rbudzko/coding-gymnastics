class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left
        maxSum = 0

        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            elif prices[right] - prices[left] > maxSum:
                maxSum = prices[right] - prices[left]
                
            right += 1
        
        return maxSum


        