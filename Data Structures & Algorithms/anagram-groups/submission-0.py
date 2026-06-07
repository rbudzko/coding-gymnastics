class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            vector = tuple(self.vectorizeStr(s))

            group = groups.get(vector, [])
            group.append(s)
            groups[vector] = group

        return list(groups.values())

    def vectorizeStr(self, s: str) -> Dict[str, int]:
        vector = [0] * 26

        for char in s:
            vector[self.charIdx(char)] += 1

        return vector

    def charIdx(self, char: str) -> int:
        return ord(char) - ord('a')