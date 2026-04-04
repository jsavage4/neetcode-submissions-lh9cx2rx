class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mostCommon = ''
        maxLength = 0
        right, left = 0, 0
        freq = {}
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            if freq[s[right]] > freq.get(mostCommon, 0):
                mostCommon = s[right]
            while right - left + 1 - freq[mostCommon] > k:
                freq[s[left]] -= 1
                if s[left] == mostCommon:
                    mostCommon = max(freq, key=freq.get)
                left += 1
            maxLength = max(maxLength, right - left + 1)
            right += 1
        
        return maxLength