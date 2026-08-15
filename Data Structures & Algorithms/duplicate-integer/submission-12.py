class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length_arr = len(nums)
        arr_check = len(set(nums))
        
        if length_arr != arr_check:
            return True
        else:
            return False
