class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in track:
                return [track[missing],i]
            track[nums[i]] = i
        
