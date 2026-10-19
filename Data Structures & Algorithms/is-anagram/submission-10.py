class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## What is an anagram?

        ## An anagram is two words that contain the same characters with each char appearing the same number of times

        ## RULES:
        ## 1. If the length of str s and str t differ than these are not anagrams of each other
        ## 2. str s and str t must have the same number of chars, if they differ than they are not anagrams
        

        ## How can we solve this?

        ## We can do a check if the length fo the 2 strs are equal, if not then return False, else continue
        if len(s) != len(t):
            return False

        ## Store the the respective char -> count relation for each char within their own respective string
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for s_char in s:
            s_dict[s_char] += 1

        for t_char in t:
            t_dict[t_char] += 1
        

        ## iterate over this mapping and make sure they don't differ / the counts are the same

        return s_dict == t_dict

