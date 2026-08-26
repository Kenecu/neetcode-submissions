class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            count[nums[i]] += 1
        for val, cnt in count.items():
            freq[cnt].append(val)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res
       
            

                
                

        
