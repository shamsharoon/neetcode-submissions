class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # basically we want to use a dictonary
        # key the number and value is the frequency of that #

        freqDict = {}

        for num in nums:
            freqDict[num] = 1 + freqDict.get(num, 0)
        
        # sort dsc and return K top keys

        newDict = dict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))

        result = []

        for i, key in enumerate(newDict.keys()):
            result.append(key)
        
        return result[0:k]