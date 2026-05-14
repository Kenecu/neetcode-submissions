class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashtable
        #set a loop through nums
        #subtract the value of numbs from target and set a variable
        #check if value is in hashtable, if it is return it
        #if value isn't in hashtable, add the value and index

        numbers = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in numbers:
                return [numbers[needed],i]
            else:
                numbers[nums[i]] = i 