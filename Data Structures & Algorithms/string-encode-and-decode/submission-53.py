class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            length = str(len(string))
            res = res + length + "#" + string
        return res
        
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+length + 1]
            result.append(word)
            i = j + length + 1
            
        return result

            
