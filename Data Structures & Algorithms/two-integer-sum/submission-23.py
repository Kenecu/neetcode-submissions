class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in check:
                return [check[j], i]
            check[nums[i]] = i
