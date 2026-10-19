class Solution:
    def isPalindrome(self, s: str) -> bool:
        # account for nums??
        resultStr = ""

        # lowercase string
        lowerS = s.lower()

        # iterate through each char and make sure it is alpha 
        # numeric
        for c in lowerS:
            if (97 <= ord(c) <= 122) or (48 <= ord(c) <= 57):
                resultStr+=c

        # reverse and check if equal backwards and forward
        return resultStr == resultStr[::-1]