class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for key, value in counts.items():
            buckets[value].append(key)

        most_frequent = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                most_frequent.append(num)

                if len(most_frequent) == k:
                    return most_frequent
        
        return most_frequent