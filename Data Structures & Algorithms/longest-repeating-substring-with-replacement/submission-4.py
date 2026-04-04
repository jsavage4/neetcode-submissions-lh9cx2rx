class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        right, left = 0, 0
        freq = {}
        maxFreq = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])
            if right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
            right += 1
        
        return right - left