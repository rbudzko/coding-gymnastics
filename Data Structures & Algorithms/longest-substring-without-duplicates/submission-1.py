class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        in_window = set()

        while right < len(s):
            while s[right] in in_window:
                in_window.discard(s[left])
                left += 1

            in_window.add(s[right])

            right += 1
            max_length = max(max_length, right - left)

        return max_length
