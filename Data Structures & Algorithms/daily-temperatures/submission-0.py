class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tps = temperatures
        res = [0] * len(tps)

        des = [] # decreasing monotonic stack

        for i in range(0, len(tps)):
            while des and tps[des[-1]] < tps[i]:
                st = des.pop()
                res[st] = i - st
            des.append(i)
        
        return res
