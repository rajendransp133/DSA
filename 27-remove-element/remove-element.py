class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        left=0
        right=len(nums)-1

        while(left<=right):
            if(nums[left]==val):
                nums[left]="_"
                nums[left],nums[right]=nums[right],nums[left]
                count+=1 
                right-=1
            else:
                left+=1         

        return len(nums)-count

        