class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for c in s:
            dict1[c] = 1 if dict1.get(c) is None else dict1[c]+1
        for c in t:
            dict2[c] = 1 if dict2.get(c) is None else dict2[c]+1
        return dict1 == dict2

        '''
        SOLUTION

        if len(s)!=len(t): return False

        dictS, dictT = {}, {}
        for i in range(len(s)):
            dictS[s[i]] = 1+dictS.get(s[i],0)
            dictT[t[i]] = 1+dictT.get(t[i],0)
        return dictS==dictT

        '''
        
