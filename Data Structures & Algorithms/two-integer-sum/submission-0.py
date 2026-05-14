class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #if the num is greater than target ignore, else
        #put nums in a hashtable
        #then iterate over them and add and see if it equals to target
        #then we grab the indices
        #return the pair of indices
        numbers = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in numbers:
                return [numbers[needed],i]
            else:
                numbers[nums[i]] = i





        