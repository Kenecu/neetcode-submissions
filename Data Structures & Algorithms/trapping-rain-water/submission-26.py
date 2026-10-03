class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        total = 0
        leftMax = height[left]
        rightMax = height[right]
        while left < right:
            if height[left] <= height[right]:
                left+=1
                leftMax = max(leftMax, height[left])
                total += leftMax - height[left]
            elif height[right] < height[left]:
                right-=1
                rightMax = max(rightMax, height[right])
                total += rightMax - height[right]
        return total