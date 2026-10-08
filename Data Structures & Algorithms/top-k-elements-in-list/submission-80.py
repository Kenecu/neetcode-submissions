class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        count_list = [[] for i in range(len(nums) + 1)]
        for number, val in count.items():
            count_list[val].append(number)

        total = []
        for i in range(len(count_list) - 1, -1, -1):
            for bucket in count_list[i]:
                total.append(bucket)
                if len(total) >= k:
                    return total
        return total




