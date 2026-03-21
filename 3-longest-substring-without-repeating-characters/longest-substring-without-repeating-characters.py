class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx=0
        i=0
        j=0
        hashmap={}
        while(i<=j and i<len(s) and j<len(s)):
            while(s[j] in hashmap):
                if(s[i] in hashmap):
                    del hashmap[s[i]]
                    i+=1
            hashmap[s[j]]=1
            maxx=max(maxx,len(hashmap))
            j+=1
        return maxx







