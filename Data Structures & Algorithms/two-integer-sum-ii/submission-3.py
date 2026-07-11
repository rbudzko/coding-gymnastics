class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        
        left = 0
        right = len(n) - 1

        while left < right:
            total = n[left] + n[right]
            
            if total == target: return [left + 1, right + 1]
            elif  total > target: right -= 1
            else: left += 1

        raise "No solution"