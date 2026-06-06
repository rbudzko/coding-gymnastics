class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        l = s.lower()

        while left < right:
            while left < right and not l[left].isalnum():
                left += 1
            while left < right and not l[right].isalnum():
                right -= 1

            if l[left] != l[right]:
                return False
            
            left += 1
            right -= 1
        
        return True