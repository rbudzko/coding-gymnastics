class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        desired = {}
        current = {}

        for char in s1:
            desired[char] = desired.get(char, 0) + 1

        while right < len(s2):
            char = s2[right]
            current[char] = current.get(char, 0) + 1

            while current.get(char, 0) > desired.get(char, 0):
                current[s2[left]] -= 1
                if current[s2[left]] < 1: del current[s2[left]]
                left += 1

            right += 1
            if desired == current: return True

        return False