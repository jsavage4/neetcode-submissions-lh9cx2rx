class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        stack.append(0)
        for idx in range(1, len(temperatures)):
            currVal = temperatures[idx]
            while stack and currVal > temperatures[stack[-1]]:
                oldIdx = stack.pop()
                ret[oldIdx] = idx - oldIdx
            stack.append(idx)
        return ret