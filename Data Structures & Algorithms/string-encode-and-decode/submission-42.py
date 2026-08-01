class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return result

        for string in strs:
            string_len = str(len(string))
            result = result + string_len + "#" + string
        return result
            

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
               j += 1
            length = int(s[i:j])
            sliced = s[j+1:j+1+length]
            result.append(sliced)
            i = length + j + 1
         
        return result



            
            
       