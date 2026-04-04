class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1C = Counter(s1)
        windowCount = Counter(s2[:len(s1)])

        if s1C == windowCount:
            return True
        
        for right in range(len(s1), len(s2)):
            windowCount[s2[right]] += 1
            left = right - len(s1)
            windowCount[s2[left]] -= 1
            if windowCount[s2[left]] == 0:
                del windowCount[s2[left]]
            if windowCount == s1C:
                return True
        return False