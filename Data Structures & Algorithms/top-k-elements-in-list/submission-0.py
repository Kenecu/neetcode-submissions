class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        count = Counter(nums)
        top_k = count.most_common(k)
        return [i[0] for i in top_k]
    