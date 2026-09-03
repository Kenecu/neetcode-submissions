class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        clean = set(nums)
        longest = 0

        for num in clean:
            if (num-1) not in clean:
                length = 1
                while (num + length) in clean:
                    length+=1
                longest = max(longest, length)
        return longest



