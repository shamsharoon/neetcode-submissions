class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        valIdx = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in valIdx:
                return [valIdx[comp], i]
            
            valIdx[nums[i]] = i