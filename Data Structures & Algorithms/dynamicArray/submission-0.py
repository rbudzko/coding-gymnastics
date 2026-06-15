class DynamicArray:
    
    array = None
    size = 0

    def __init__(self, capacity: int):
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= len(self.array):
            self.resize()

        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]       

    def resize(self) -> None:
        self.array.extend([None] * len(self.array))

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.array)
