class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_s = defaultdict(int)
        string_t = defaultdict(int)
        for i in range(len(s)):
            string_s[s[i]] += 1
        for i in range(len(t)):
            string_t[t[i]] += 1
        if string_s == string_t:
            return True
        else:
            return False