class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char={}
        output=[]
        for i in range(len(strs)):
            sort_string=''.join(sorted(strs[i]))
            if sort_string in char:
                char[sort_string].append(strs[i])
            else:
                char[sort_string]=[strs[i]]
        return list(char.values())













        
        
        
        
        

        