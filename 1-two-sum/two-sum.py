from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        new =defaultdict(int)

        for j in nums:
            new[j]+=1
        
        return_list=[]

        for i in range(len(nums)):
            diff=target-nums[i]
            if(new[nums[i]]==1):
                del new[nums[i]]
            if(diff in new.keys()):
                for k in range(i+1,len(nums)):
                    if(diff==nums[k]):
                        return_list.append(i)
                        return_list.append(k)
                        return return_list
            
            new[nums[i]]+=1
            



            
                

        