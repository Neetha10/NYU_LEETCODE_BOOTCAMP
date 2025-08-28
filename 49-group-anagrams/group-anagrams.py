class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts_list=[]
        groups=[]
        for word in strs:
            hashi={}
            for char in word:
                if char in hashi:
                    hashi[char]+=1
                else:
                    hashi[char]=1
            found=False
            for i,prev_count in enumerate(counts_list):
                if hashi==prev_count:
                    groups[i].append(word)
                    found=True
                    break
            if not found:
                counts_list.append(hashi)
                groups.append([word])
        return groups
            

        
            
            
            
            
        