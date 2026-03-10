class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0
        right =len(numbers)-1
        while(left<right):
            new_target=target-numbers[right]
            while(numbers[left]<new_target):
                left+=1
            if(numbers[left]==new_target):
                return [left+1,right+1]
            else:
                right =right -1
        