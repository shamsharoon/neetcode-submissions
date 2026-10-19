class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # what do we know?

        # KNOW: Anagram is a word that can be spelled with the letters re arranged
        # Solution: we need to make sure both words have the same # of letters 
        # and contain the same letters ONLY

        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1
        
        return sDict == tDict
