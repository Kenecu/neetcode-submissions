class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        track = defaultdict(int)
        
        longest = 0
        while right < len(s):
            track[s[right]] += 1
            if (right - left + 1) - max(track.values()) > k:
                track[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest