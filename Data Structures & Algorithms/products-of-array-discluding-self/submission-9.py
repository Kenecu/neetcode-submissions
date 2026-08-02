class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
           copy = list(nums)
           copy.pop(i)
           total = 1
           for j in copy:
            total = j * total
           output.append(total)
        return output
        
