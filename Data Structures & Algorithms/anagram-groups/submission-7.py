class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        a_dict: Dict[str, List[str]] = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in a_dict:
                a_dict[sorted_word].append(word)
            else:
                a_dict[sorted_word] = [word]

        return list(a_dict.values())