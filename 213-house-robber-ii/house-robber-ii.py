class Solution:
    def rob(self, nums: List[int]) -> int:

        if(len(nums)==1):
            return nums[0]
        
        if(len(nums)==2):
            return(max(nums[0],nums[1]))

        def rob_non_curcular(nums: List[int]) -> int:
            n=len(nums)
            if(n==1):
                return nums[0]
            for i in range(1,n):
                if((i-2)<0):
                    nums[i]=max(nums[i],nums[i-1])
                else:
                    nums[i]=max(nums[i]+nums[i-2],nums[i-1])
            return nums[-1]

        return max(rob_non_curcular(nums[1:]),rob_non_curcular(nums[:-1]))


