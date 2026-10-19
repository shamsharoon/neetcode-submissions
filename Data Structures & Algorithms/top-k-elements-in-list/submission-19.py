class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        sorted_items_desc = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        top_k_elements = [item[0] for item in sorted_items_desc[:k]]
        return top_k_elements