class Solution:

    def encode(self, strs: List[str]) -> str:
        string_final = ""
        for string in strs:
            string_final += str(len(string)) + "#" + string
        return string_final

    def decode(self, s: str) -> List[str]:
        left = 0
        total = []
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            cut = int(s[left:right])
            word = s[right + 1: right + cut + 1]
            total.append(word)
            left = right + cut + 1
            right = left + 1
        return total


            
