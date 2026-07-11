class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        
        left = 0
        right = len(n) - 1

        while n[left] + n[right] != target:
            if n[left] + n[right] > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]