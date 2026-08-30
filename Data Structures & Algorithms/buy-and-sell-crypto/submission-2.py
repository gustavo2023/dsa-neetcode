class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_buy_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_buy_price:
                min_buy_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_buy_price)

        return max_profit