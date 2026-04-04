class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complements = {'}': '{', ')': '(', ']': '['}
        for char in s:
            if char in complements:
                if not stack:
                    return False
                checkChar = stack.pop()
                if checkChar != complements[char]:
                    return False
            else:
                stack.append(char)
        return not stack