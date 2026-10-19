class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if i can seperate every charcater into their own array then sort it i can iterate through it and check if every character is the same

        sArr = []
        for letter in s:
            sArr.append(letter)

        tArr = []
        for letter in t:
            tArr.append(letter)

        return sorted(sArr) == sorted(tArr)