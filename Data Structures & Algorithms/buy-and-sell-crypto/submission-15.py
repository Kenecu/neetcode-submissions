class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        best = prices[left]
        total = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                best = prices[right]
                left = right
            total = max(total, prices[right] - best)
            right += 1
        return total

