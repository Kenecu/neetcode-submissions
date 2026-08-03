class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = defaultdict(int)
        for i in range(len(nums)):
            if check[nums[i]] == 1:
                return True
            check[nums[i]] += 1   
        return False