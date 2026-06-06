class Solution:

    delimiter = '@'

    def encode(self, strs: List[str]) -> str:
        parts = []
        
        for s in strs:
            parts.append(str(len(s)))
            parts.append(self.delimiter)
            parts.append(s)

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        strs = []
        rest = s

        while len(rest) > 0:
            head, _, rest = rest.partition(self.delimiter)
            length = int(head)
            strs.append(rest[:length])
            rest = rest[length:]

        return strs

