class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left <= right:
            if not s[right].isalpha() and not s[right].isdigit():
                right -= 1
                continue
            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
                continue
            if s[left] != s[right]:
                return False
            right -= 1
            left += 1
        
        return True