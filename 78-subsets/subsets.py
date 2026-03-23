class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        final_return_list=[[]]

        def recursion(arr,num):
            final_return_list_updated=[]
            for j in arr:
                final_return_list_updated.append(j.copy())
                j.append(num)
                final_return_list_updated.append(j)
            return final_return_list_updated

        for i in nums:
            final_return_list=recursion(final_return_list,i)

        return final_return_list

