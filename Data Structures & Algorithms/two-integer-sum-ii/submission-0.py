class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force method O(n^2): iterate through the entire array until we find two nums that add
        # up to the target. check if index1 < index2

        # ill implement this first then the optimized solution

        for index1 in range(len(numbers)):
            for index2 in range(index1+1, len(numbers)):
                if (numbers[index1] + numbers[index2] == target) and (index1 < index2):
                    return [index1+1, index2+1]






        # O(n log n): use binary search to split half the problem in half by
        # finding which half is smaller than the target value

        # once we find what half to work on keep doing binary search to find two items that
        # add up to the target then check if the index1 < index2

