class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        elementIndex = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            # check if the complement if in the dictonary
            if complement in elementIndex:
                return [elementIndex[complement], i]
            
            # if not in the dict then keep adding pairs
            elementIndex[nums[i]] = i
        return [-1]