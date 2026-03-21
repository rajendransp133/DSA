class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_arr=[0]*26
        freq_arr2=[0]*26
        for i in s1:
            freq_arr[ord(i)-97]+=1
        fixed_window=len(s1)
        if(len(s2)>=fixed_window):
            for j in range(fixed_window):
                freq_arr2[ord(s2[j])-97]+=1
            if(freq_arr==freq_arr2):
                return True
            print(fixed_window)
            for k in range(fixed_window,len(s2)):
                freq_arr2[ord(s2[k-fixed_window])-97]-=1
                freq_arr2[ord(s2[k])-97]+=1
                if(freq_arr==freq_arr2):
                    return True
        return False



           
        



        


