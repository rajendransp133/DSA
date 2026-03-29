class Solution:
    def countBits(self, n: int) -> List[int]:
        if(n==0):
            return [0]
        if(n==1):
            return [0,1]
        return_arr=[0,1]
        for i in range(2,n+1):
            floor_log= math.floor(math.log2(i))
            return_arr.append(return_arr[i%(2**floor_log)]+1)
        return return_arr


        