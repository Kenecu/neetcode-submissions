class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            group[nums[i]] +=1
        for key,value in group.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

