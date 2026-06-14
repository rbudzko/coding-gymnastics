class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for day in range(0, len(prices) - 1):
            if prices[day + 1] > prices[day]:
                profit += prices[day + 1] - prices[day]

        return profit