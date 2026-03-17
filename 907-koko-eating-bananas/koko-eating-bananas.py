import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ceil_left=math.ceil(sum(piles)/h)
        ceil_right = math.ceil(max(piles)) +1

        def check_func(div):
            output_iterator = map(lambda x : math.ceil(x/div), piles)
            if(sum(list(output_iterator))<=h):
                return True
            else:
                return False
        curr_global=-1

        while(ceil_left<ceil_right):
            mid = (ceil_left + ceil_right) //2
            if(check_func(mid)):
                curr_global=mid
                ceil_right=mid
            else:
                ceil_left=mid+1

        return curr_global