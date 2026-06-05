class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for n in nums[1:]:
            if curSum < 0:
                curSum = 0
            
            curSum = curSum + n
            
            if curSum > maxSum:
                maxSum = curSum
    
        return maxSum
