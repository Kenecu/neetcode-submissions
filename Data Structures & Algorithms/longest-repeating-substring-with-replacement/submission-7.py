class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        freq = defaultdict(int)
        length = 0
        while right < len(s):
            freq[s[right]] += 1
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left +=1
            length = max(length, right - left + 1)
            right+=1
        return length



        