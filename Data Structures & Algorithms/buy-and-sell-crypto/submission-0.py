class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            current_profit = 0

            if prices[i] < min_price:
                min_price = prices[i]
            else:
                current_profit = prices[i] - min_price

            max_profit = max(max_profit, current_profit)

        return max_profit    