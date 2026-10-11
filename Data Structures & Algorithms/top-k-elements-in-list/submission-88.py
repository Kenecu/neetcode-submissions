class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        count_list = [[] for i in range(len(nums) + 1)]
        for key, val in count.items():
            count_list[val].append(key)

        ans = []
        for i in range(len(count_list) - 1, -1, -1):
            for answer in count_list[i]:
                if len(ans) >= k:
                    return ans
                ans.append(answer)
        return ans
