class Solution:

    def encode(self, strs: List[str]) -> str:
        retStr = ''.join(strs)
        for myStr in reversed(strs):
            retStr = f'{len(myStr)}.' + retStr
        retStr = f'{len(strs)}.' + retStr
        return retStr

    def decode(self, s: str) -> List[str]:
        lengths = s.split('.')
        strLengths = lengths[1:int(lengths[0])+1]

        encodedStr = ''.join(lengths[int(lengths[0])+1:])
        strs = []
        idx = 0
        for strLength in strLengths:
            strs.append(encodedStr[idx:idx+int(strLength)])
            idx += int(strLength)
        
        return strs

