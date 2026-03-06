class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        li=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while(left<right):
                currs_sum=nums[i]+nums[left]+nums[right] 
                if(currs_sum==0):
                    li.append([nums[i], nums[left], nums[right]])
                    left=left+1
                    right=right-1
                elif(currs_sum<0):
                    left=left+1
                else:
                    right=right-1
        return [list(i) for i in set(tuple(x) for x in li)]
        