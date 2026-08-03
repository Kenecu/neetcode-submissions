class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for i in range(1,len(nums)):
            prefix = result[i-1] * nums[i-1]
            result.append(prefix)
        multi = 1
        for i in range(len(nums)-1,0,-1):
            multi = multi * nums[i]
            result[i-1] = result[i-1] * multi
        return result