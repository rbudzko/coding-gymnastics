class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        ranking = [[] for _ in range(len(nums) + 1)]
        
        for key, value in counts.items():
            ranking[value].append(key)

        results = []

        for rank in reversed(ranking):
            results.extend(rank)

        return results[:k]
        