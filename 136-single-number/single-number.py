class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_result=0
        for i in nums:
            xor_result = xor_result ^ i
        return(xor_result) 

        