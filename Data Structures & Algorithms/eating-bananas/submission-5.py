class Solution:
    def eat(self, piles: List[int], h: int, k: int) -> bool:
        counter = 0
        for pile in piles:
            counter += pile // k
            if pile % k != 0: counter += 1
        return counter <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        last = 1

        while left <= right:
            k = (left + right) // 2
            if self.eat(piles, h, k): 
                last = k
                right = k - 1
            else:
                left = k + 1

        return last