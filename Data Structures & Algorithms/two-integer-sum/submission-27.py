class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in values:
                return [values[val], i]
            values[nums[i]] = i
        
        