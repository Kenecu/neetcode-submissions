class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list) 

        for word in strs:
            label = [0] * 26
            for char in word:
                label[ord(char) - ord("a")] += 1
            check[tuple(label)].append(word)
        return list(check.values())

    
        
