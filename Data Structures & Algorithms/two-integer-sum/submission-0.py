class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()

        for idx, val in enumerate(nums):
            diff = target - val
            
            if diff in diffs:
                return [diffs[diff], idx]
            diffs[val] = idx

        return list()