class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==0):
            return 0
        maxx=0
        i=0
        j=1
        while(i<j and j<len(prices)):
            if(prices[j]-prices[i]>0):
                maxx=max(prices[j]-prices[i],maxx)
            else:
                i=j
            j+=1
        return maxx
