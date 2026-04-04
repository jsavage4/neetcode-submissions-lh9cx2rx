class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength  = 0
        currWindow = set()
        left = 0

        for right in range(len(s)):
            if s[right] in currWindow:
                while s[right] in currWindow:
                    currWindow.remove(s[left])
                    left += 1
            currWindow.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
            
