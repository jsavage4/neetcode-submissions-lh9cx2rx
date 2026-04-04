class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retStrs = defaultdict(list)
        for currStr in strs:
            key = tuple(sorted(currStr))
            retStrs[key].append(currStr)
        
        return list(retStrs.values())