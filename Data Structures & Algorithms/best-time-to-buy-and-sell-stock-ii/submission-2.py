class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = None

        for day in range(0, len(prices) - 1):
            if bought == None and prices[day + 1] > prices[day]:
                bought = prices[day]
            elif bought != None and prices[day + 1] < prices[day]:
                profit += prices[day] - bought
                bought = None
        
        if bought != None:
            profit += prices[len(prices) - 1] - bought

        return profit