class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force Solution?
        # We iterate through every element in
        # a nested for loop and multi everything except
        # the curr element

        result = []

        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j != i:
                    total = total*nums[j]
            result.append(total)
        return result
