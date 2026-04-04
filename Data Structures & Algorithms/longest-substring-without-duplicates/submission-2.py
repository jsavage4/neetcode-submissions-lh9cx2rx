class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength, currLength = 0, 0
        currentWindow = set()
        left, right = 0,0

        while right < len(s):
            if s[right] in currentWindow:
                while s[left] != s[right]:
                    currentWindow.remove(s[left])
                    currLength -= 1
                    left += 1
                left += 1
                currLength -= 1
            currentWindow.add(s[right])
            currLength += 1
            right += 1
            maxLength = max(maxLength, currLength)

        return maxLength
            
