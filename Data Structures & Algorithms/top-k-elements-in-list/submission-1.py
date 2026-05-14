class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a hashmap to count freq of each num
        #create a empty list with empty lists corr to # len of nums
        #grab key value pair, append the value to the list

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for value, n in count.items():
            freq[n].append(value)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
               
                
               
                    




