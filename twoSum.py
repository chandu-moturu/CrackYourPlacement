class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        duck = {}  
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in duck:
                return [duck[complement], i]
            duck[num] = i
        return []