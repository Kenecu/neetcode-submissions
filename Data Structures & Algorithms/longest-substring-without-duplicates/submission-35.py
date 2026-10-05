class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        substring = set()
        longest = 0
        while right < len(s):
            while s[right] in substring:
                substring.remove(s[left])
                left+=1
            substring.add(s[right])
            longest = max(longest, len(substring))
            right += 1
        return longest

