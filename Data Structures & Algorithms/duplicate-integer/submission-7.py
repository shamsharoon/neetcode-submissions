class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set, if the set is different we know we had a duplicate
        # use a 2 pointer and go through the array to see if there are any dupes
        # sort the arr and then check the neighbours to see if there are any dupes 

        return len(set(nums)) != len(nums)