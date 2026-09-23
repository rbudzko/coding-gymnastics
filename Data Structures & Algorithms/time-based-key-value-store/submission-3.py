class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        td = self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        td = self.cache[key]

        left, right = 0, len(td) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= td[mid][0]:
                left = mid + 1
                result = td[mid][1]
            else:
                right = mid - 1

        return result
        