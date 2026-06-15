class Solution:
    def _calc(self, left: str, right: str, operator: str) -> int:
        if operator == "/": return int(left / right)
        if operator == "*": return int(left * right)
        if operator == "+": return int(left + right)
        if operator == "-": return int(left - right)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["/", "*", "+", "-"]:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(self._calc(left, right, token))

        return stack.pop()