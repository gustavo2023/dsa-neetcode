class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_selling_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_selling_price:
                min_selling_price = prices[i]
            else:
                profit = prices[i] - min_selling_price
                max_profit = max(max_profit, profit)

        return max_profit