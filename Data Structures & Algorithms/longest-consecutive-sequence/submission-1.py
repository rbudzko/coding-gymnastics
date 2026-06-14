class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        maxCount = 0

        for num in cache:
            if num - 1 in nums: continue

            count = 0
            while num in cache:
                num += 1
                count += 1
            
            maxCount = max(count, maxCount)
        
        return maxCount
        