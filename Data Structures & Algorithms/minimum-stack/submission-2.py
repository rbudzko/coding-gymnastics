class MinStack:

    def __init__(self):
        self.mainStack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        newMin = val if not self.minStack or self.minStack[0] >= val else self.minStack[0]
        self.mainStack.appendleft(val)
        self.minStack.appendleft(newMin)
        
    def pop(self) -> None:
        self.minStack.popleft()
        self.mainStack.popleft()

    def top(self) -> int:
        return self.mainStack[0]
        
    def getMin(self) -> int:
        return self.minStack[0]
