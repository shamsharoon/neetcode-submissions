class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        mostFreqDict = {}

        for num in nums:
            mostFreqDict[num] = mostFreqDict.get(num, 0) + 1

        sorted_dict = dict(sorted(mostFreqDict.items(), key=lambda item: item[1], reverse=True))

        listNums = []

        listNums.extend(list(sorted_dict.keys())[:k])

        return listNums
