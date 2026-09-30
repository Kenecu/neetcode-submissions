class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        total = 0
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax <= rightMax:
                total += leftMax - height[left]
                left+=1
                leftMax = max(leftMax,height[left])
            elif rightMax < leftMax:
                total += rightMax - height[right]
                right-=1
                rightMax = max(rightMax,height[right])
            

        return total




            