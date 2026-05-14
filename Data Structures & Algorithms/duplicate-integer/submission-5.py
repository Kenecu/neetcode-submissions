class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for i in nums:
            if i not in numbers:
                numbers.add(i)
            elif i in numbers:
                return True
        return False
         