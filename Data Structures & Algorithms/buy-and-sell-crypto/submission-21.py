class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = 0
        left = 0
        right = 1
        best_day = prices[left]

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                best_day = prices[left]
            cost = prices[right] - best_day
            best_price = max(best_price, cost)
            right += 1
        return best_price