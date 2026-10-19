class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if target inside of dict then return i and dict[key]

        valueIndex = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in valueIndex:
                return [valueIndex[comp], i]
            
            valueIndex[nums[i]] = i