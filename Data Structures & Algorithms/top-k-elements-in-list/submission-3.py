class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        for key, value in frequencies.items():
            buckets[value].append(key)

        top_frequent = []

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                top_frequent.append(num)

                if len(top_frequent) == k:
                    return top_frequent

        