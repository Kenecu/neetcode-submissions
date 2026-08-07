class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            counter[nums[i]] += 1
        for key, value in counter.items():
            freq[value].append(key)

        res = []
        for i in range(len(nums),0,-1):
            for value in freq[i]:
                res.append(value)
                if len(res) == k:
                    return res
