class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringOne = defaultdict(int)
        stringTwo = defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            stringOne[s[i]] += 1
            stringTwo[t[i]] += 1

        return stringOne == stringTwo
        

