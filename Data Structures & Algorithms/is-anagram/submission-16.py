class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for char in s:
            s_count[char] += 1
        for char in t:
            t_count[char] += 1

        if s_count == t_count:
            return True
        else:
            return False