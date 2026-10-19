class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNum = {}

        for num in nums:
            freqNum[num] = 1 + freqNum.get(num, 0)

        sorted_items = sorted(freqNum.items(), key=lambda item: item[1], reverse=True)
        top_k = [item[0] for item in sorted_items[:k]]

        return top_k
