class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = defaultdict(int)
        for i in range(len(nums)):
            duplicate[nums[i]] += 1
            if duplicate[nums[i]] > 1:
                return True
        return False