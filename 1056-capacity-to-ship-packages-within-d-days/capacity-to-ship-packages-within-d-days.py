class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left= math.ceil(sum(weights)//days)
        right=sum(weights)

        def check_enough(val,days):
            count=0
            for i in range(len(weights)):
                count+=weights[i]
                while(count>val and days>0):
                    count=weights[i]
                    days-=1
                if(days==0):
                    return False
            return True


        while(left<right):
            mid=(left+right)//2
            if(check_enough(mid,days)):
                right=mid
            else:
                left=mid+1
        return left
