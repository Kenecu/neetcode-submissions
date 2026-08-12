class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
            
        for i in range(len(strs)):
            length = str(len(strs[i]))
            res = res + length + "#" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
            
        i = 0
        result = []
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:length+j+1]
            result.append(word)
            i = j + length + 1
        return result


