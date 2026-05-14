class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap
        #loop through each words in the string
        #create a list to hold 26 letters
        #loop through each letter in the string
        #add a count when you encounter a letter and add to hashmap
        #then add the word when the count matches a key
        #return the values of the hashmap
        letters = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i)-ord("a")] += 1
                
            letters[tuple(count)].append(s)
            
        return list(letters.values())