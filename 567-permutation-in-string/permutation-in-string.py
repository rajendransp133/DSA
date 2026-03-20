class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap={}
        for i in s1:
            if(i in hashmap):
                hashmap[i]+=1
            else:
                hashmap[i]=1
        hashmap2=hashmap.copy()
        for i in range(len(s2)):
            if(s2[i] in hashmap):
                hashmap[s2[i]]-=1
                if(hashmap[s2[i]]==0):
                    del hashmap[s2[i]]
                j=i+1
                while(j<len(s2) and s2[j] in hashmap):
                    hashmap[s2[j]]-=1
                    if(hashmap[s2[j]]==0):
                        del hashmap[s2[j]]
                        
                    j+=1
            if(len(hashmap)==0):
                return True
            else:
                hashmap=hashmap2.copy()
        return False



        


