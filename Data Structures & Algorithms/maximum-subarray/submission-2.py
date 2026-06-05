class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for n in nums[1:]:    
            curSum = max(0, curSum)
            curSum = curSum + n
            maxSum = max(maxSum, curSum)
    
        return maxSum
