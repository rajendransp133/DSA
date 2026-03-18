class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in range(len(nums)):
            if(nums[i]==val):
                nums[i]="_"
            else:
                count+=1
        left=0
        right=len(nums)-1
        while(left<right):
            if(nums[left]=="_"):
                nums[left],nums[right]=nums[right],nums[left]
                right-=1
            else:
                left+=1            

        return count

        