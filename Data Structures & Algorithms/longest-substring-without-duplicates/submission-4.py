class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right, left = 0, 0
        maxLength = 0
        currWindow = set()

        while right < len(s):
            while s[right] in currWindow:
                currWindow.remove(s[left])
                left += 1
            currWindow.add(s[right])
            maxLength = max(maxLength, right - left + 1)
            right += 1
        return maxLength