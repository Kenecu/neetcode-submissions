class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res = res + str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:length + j + 1]
            result.append(word)
            i = length + j + 1
        return result
            
                
            
            
