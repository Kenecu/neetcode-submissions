class Solution:

    def encode(self, strs: List[str]) -> str:
        connect = ""
        for word in strs:
            connect += str(len(word)) + "#" + word
        return connect
    def decode(self, s: str) -> List[str]:
        total = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            start = right  + 1
            total.append(s[start : start + length])
            left = right + length + 1
        return total



    

        
            
