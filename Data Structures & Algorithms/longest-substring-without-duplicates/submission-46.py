class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = set()
        left = 0
        right = 0

        total = 0
        while right < len(s):
            while s[right] in track:
                track.remove(s[left])
                left += 1
            track.add(s[right])
            total = max(total, len(track))
            right += 1
        return total
      