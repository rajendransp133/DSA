class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_val=10000000
        i=0
        curr_sum=0
        for j in range(len(nums)):
            curr_sum+=nums[j]
            print(i,j)
            while(curr_sum>=target):
                min_val=min(min_val,j-i+1)
                curr_sum -= nums[i]
                i+=1
        if(min_val==10000000):
            min_val=0
        return min_val
        # i=0
        # j=len(nums)
        # min_val=10000000
        # while(i<j):
        #     if(sum(nums[i:j])>=target):
        #         min_val=min(min_val,j-i)
        #     if(nums[i]>nums[j-1]):
        #         j-=1
        #     else:
        #         i+=1
        # if(min_val==10000000):
        #     min_val=0
        # return min_val
        