class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left = 0
        freq = {}
        maxFreq = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
        
        return right - left + 1