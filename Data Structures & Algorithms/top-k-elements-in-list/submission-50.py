class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for number in nums:
            count[number] += 1
        for num, con in count.items():
            freq[con].append(num)
        
        res = []
        for i in range(len(nums),0, -1):
            for item in freq[i]:
                if len(res) == k:
                    return res
                res.append(item)
        return res
                
        


