class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = 0
        right, left = 0, 0
        tCount = Counter(t)
        retString = ''

        while right < len(s):
            if s[right] in tCount:
                tCount[s[right]] -= 1      # consume the requirement
                if tCount[s[right]] >= 0:  # only count if it was actually needed
                    count += 1

            while count == len(t):         # valid window — try to shrink
                currRetString = s[left:right+1]
                if len(currRetString) < len(retString) or retString == '':
                    retString = currRetString

                if s[left] in tCount:
                    tCount[s[left]] += 1   # restore the requirement
                    if tCount[s[left]] > 0:
                        count -= 1         # window no longer valid
                left += 1

            right += 1

        return retString