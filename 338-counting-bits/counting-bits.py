class Solution:
    def countBits(self, n: int) -> List[int]:
        return_arr=[0,1]
        if(n==0):
            return [0]
        if(n==1):
            return return_arr
        curr_floor=1
        for i in range(2,n+1):
            offset=i%curr_floor
            if(offset== 0):
                curr_floor*=2
            return_arr.append(return_arr[offset]+1)

        return return_arr


        