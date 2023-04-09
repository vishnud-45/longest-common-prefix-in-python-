class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return s[0]
        else:
            s.sort()
            l=""
            for i in range(len(s[0])):
                if(s[0][i]==s[-1][i]):
                    l=l+s[0][i]
                else:
                    break
        return l
