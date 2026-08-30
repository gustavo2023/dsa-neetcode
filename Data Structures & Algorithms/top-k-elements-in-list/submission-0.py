class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            frequency_map[n] = frequency_map.get(n, 0) + 1
        
        for key, value in frequency_map.items():
            buckets[value].append(key)

        most_frequent = []

        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                most_frequent.append(n)

                if len(most_frequent) == k:
                    return most_frequent

        return most_frequent

        