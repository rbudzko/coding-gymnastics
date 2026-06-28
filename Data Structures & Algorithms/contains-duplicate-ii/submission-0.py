class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        remembered = set()
        left_idx = 0

        for right_val in nums:
            if right_val in remembered: return True
            
            remembered.add(right_val)

            if len(remembered) > k:
                remembered.remove(nums[left_idx])
                left_idx += 1

        return False