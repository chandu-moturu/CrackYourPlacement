class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        p=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                nums.remove(nums[i])
                p.append(i)
        
        for i in range(len(p)):
            nums.append(0)

        