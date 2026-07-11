class Solution:
    def trap(self, height: List[int]) -> int:       
        h = height
        area = 0

        left = 0
        right = len(h) - 1

        left_max = h[left]
        right_max = h[right]
               

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, h[left])
                area += left_max - h[left]
            else:
                right -= 1
                right_max = max(right_max, h[right])
                area += right_max - h[right]
        
        return area