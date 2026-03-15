from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        global_dic = defaultdict(list)
        for j in strs:
            new=[0]*26
            for i in j:
                new[ord(i)-97]+=1
            global_dic[tuple(new)].append(j)
        return list(global_dic.values())
            

