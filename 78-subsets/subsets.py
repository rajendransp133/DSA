class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        final_return_list=[[]]

        def recursion(arr,num):
            n=len(arr)
            for j in arr[:n]:
                j_new=j.copy()
                j_new.append(num)
                arr.append(j_new)
            return arr

        for i in nums:
            final_return_list=recursion(final_return_list,i)

        return final_return_list

