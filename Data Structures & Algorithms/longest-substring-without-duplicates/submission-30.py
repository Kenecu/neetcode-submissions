class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0 

        longest = set()
        total = 0
        while right < len(s):
            while s[right] in longest:
                longest.remove(s[left])
                left+=1
            longest.add(s[right])
            total = max(total,len(longest))
            right+=1
        return total
