class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_lvl = 0
        while left < right:
            lvl = (right - left) * min(heights[left], heights[right])
            max_lvl = max(max_lvl, lvl)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_lvl