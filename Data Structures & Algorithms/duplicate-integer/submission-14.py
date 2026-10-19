class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## Iterate through the entire list of integers
        ## Add to a set
        ## if item already in set return True
        ## if we finish iteration and no item has a conflict return False for no Duplicates

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False