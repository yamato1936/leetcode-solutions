class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profits = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profits = max(max_profits, price - min_price)

        return max_profits
