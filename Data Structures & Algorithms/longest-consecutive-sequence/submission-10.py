class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cleaned = set(nums)
        longest = 0

        for num in cleaned:
            if num-1 not in cleaned:
                length = 0
                while num + length in cleaned:
                    length+=1
                longest = max(longest, length)
        return longest
            


