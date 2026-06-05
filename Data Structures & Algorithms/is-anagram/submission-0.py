class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()

        for char in s:
            seen[char] = seen.get(char, 0) + 1
        
        for char in t:
            seen[char] = seen.get(char, 0) - 1

        for key in seen:
            if seen.get(key, 0) != 0:
                return False
        
        return True