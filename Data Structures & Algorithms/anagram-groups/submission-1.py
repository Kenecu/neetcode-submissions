class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_str = defaultdict(list)
        for s in strs:
            sorts = ''.join(sorted(s))
            sort_str[sorts].append(s)
        return list(sort_str.values())


