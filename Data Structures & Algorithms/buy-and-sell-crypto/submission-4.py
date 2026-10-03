class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        best = prices[left]
        profit = 0
        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
                best = prices[left]

            right += 1

        return profit