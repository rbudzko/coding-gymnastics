class Solution:
    def _calc(self, left: str, right: str, operator: str) -> int:
        if operator == "/": return int(left) / int(right)
        if operator == "*": return int(left) * int(right)
        if operator == "+": return int(left) + int(right)
        if operator == "-": return int(left) - int(right)

    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()

        for token in tokens:
            if token not in ["/", "*", "+", "-"]:
                dq.appendleft(token)
            else:
                right = dq.popleft()
                left = dq.popleft()
                dq.appendleft(self._calc(left, right, token))

        return int(dq.popleft())