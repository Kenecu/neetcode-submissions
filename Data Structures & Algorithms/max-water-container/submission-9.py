class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        total = 0
        while left < right:
            width = right - left
            height = min(heights[right],heights[left])
            total = max(total,width * height)
            
            if heights[left] > heights[right]:
                right-=1
            elif heights[right] > heights[left]:
                left+=1
            elif heights[right] == heights[left]:
                left+=1

        return total
           
            


