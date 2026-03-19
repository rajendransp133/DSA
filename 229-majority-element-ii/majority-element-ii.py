from collections import defaultdict 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target= len(nums)//3
        count_dict=defaultdict(int)
        return_arr=[]
        for i in nums:
            if(count_dict[i]>target):
                pass
            else:
                count_dict[i]+=1
                if(count_dict[i]>target):
                    return_arr.append(i)
        return return_arr
