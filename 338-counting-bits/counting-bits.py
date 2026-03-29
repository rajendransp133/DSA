class Solution:
    def countBits(self, n: int) -> List[int]:
        if(n==0):
            return [0]
        if(n==1):
            return [0,1]
        return_arr=[0,1]
        curr_floor=1
        for i in range(2,n+1):
            if(i%curr_floor == 0):
                curr_floor*=2
            return_arr.append(return_arr[i%curr_floor]+1)

        return return_arr


        