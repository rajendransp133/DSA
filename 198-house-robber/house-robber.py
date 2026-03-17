class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if((i-2)<0):
                nums[i]=max(nums[i],nums[i-1])
            else:
                nums[i]=max(nums[i]+nums[i-2],nums[i-1])
        print(nums)
        return nums[-1]