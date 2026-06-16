class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)

            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                first = stack.pop()
                second = stack.pop()
                
                if abs(first) > abs(second): stack.append(first)
                elif abs(second) > abs(first): stack.append(second)
        
        return stack

[-2,-1,1,2]
[]
