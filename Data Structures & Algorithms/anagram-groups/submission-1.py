class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retStrs = defaultdict(list)
        for currStr in strs:
            count = [0] * 26
            for c in currStr:
                count[ord(c) - ord('a')] += 1
            retStrs[tuple(count)].append(currStr)
        return list(retStrs.values())