class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        for i in range(l-1,-1,-1):
            if(nums.count(nums[i])>1):
                nums.remove(nums[i])
        print(nums)