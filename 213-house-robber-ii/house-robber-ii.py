class Solution:
    def rob(self, nums: List[int]) -> int:

        if(len(nums)==1):
            return nums[0]

        new_dp_array=[0]*len(nums)
        new_dp_array[0]=(nums[0],[0])

        for i in range(1,len(nums)):
            if(i-2<0):
                if(nums[i]>new_dp_array[i-1][0]):
                    new_dp_array[i]=(nums[i],[i])
                else:
                    new_dp_array[i-1][1].append(i)
                    new_dp_array[i]=(new_dp_array[i-1][0],new_dp_array[i-1][1])
            else:
                if(nums[i]+new_dp_array[i-2][0]>new_dp_array[i-1][0]):
                    new_dp_array[i-2][1].append(i)
                    new_dp_array[i]=(nums[i]+new_dp_array[i-2][0],new_dp_array[i-2][1])
                else:
                    new_dp_array[i-1][1].append(i)
                    new_dp_array[i]=(new_dp_array[i-1][0],new_dp_array[i-1][1])

        def rob_non_curcular(nums: List[int]) -> int:
            for i in range(1,len(nums)):
                if((i-2)<0):
                    nums[i]=max(nums[i],nums[i-1])
                else:
                    nums[i]=max(nums[i]+nums[i-2],nums[i-1])
            return nums[-1]

        if(0 in new_dp_array[-1][1] and (len(nums)-1) in new_dp_array[-1][1]):
            return max(rob_non_curcular(nums[1:]),rob_non_curcular(nums[:-1]))
        else:
            return new_dp_array[-1][0]

