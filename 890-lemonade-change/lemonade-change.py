class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap={5:0,10:0,20:0}
        for i in bills:
            if(i==5):
                hashmap[5]+=1
            elif(i==10):
                if(hashmap[5]==0):
                    return False
                else:
                    hashmap[10]+=1
                    hashmap[5]-=1
            else:
                if(hashmap[10]>0 and hashmap[5]>0):
                    hashmap[10]-=1
                    hashmap[5]-=1
                elif(hashmap[10]==0 and hashmap[5]>=3):
                    hashmap[5]-=3
                else:
                    return False
        return True

        