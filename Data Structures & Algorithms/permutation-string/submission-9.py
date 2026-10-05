class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        for char in s1:
            s1_count[char] += 1

        left = 0
        right = 0
        while right < len(s2):
            if right - left >= len(s1):
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left+=1
            s2_count[s2[right]] += 1
            right+=1
            if s1_count == s2_count:
                return True
        return False

        