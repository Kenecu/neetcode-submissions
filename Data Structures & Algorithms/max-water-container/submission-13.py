class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        total = 0
        while left < right:
            height = min(heights[left], heights[right])
            width  = right - left
            total = max(total, height * width)

            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            
        return total

