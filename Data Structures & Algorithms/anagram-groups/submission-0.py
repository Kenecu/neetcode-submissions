class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = {}
        for i in range(len(strs)):
            sort_str = ''.join(sorted(strs[i]))
            if sort_str in sort:
                sort[sort_str].append(strs[i])
            else:
                sort[sort_str] = [strs[i]]
        return list(sort.values())
            

