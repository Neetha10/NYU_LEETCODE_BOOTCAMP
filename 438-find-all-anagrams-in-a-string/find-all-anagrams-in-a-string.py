class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        dicti={}
        k=len(p)
        output=[]
        window={}
        for i in range(k):
            dicti[p[i]]=dicti.get(p[i],0)+1
        for i in range(k):
            window[s[i]] = window.get(s[i], 0) + 1
        if window==dicti:
            output.append(0)
        for i in range(k,len(s)):
            window[s[i-k]]-=1
            if window[s[i-k]]==0:
                del window[s[i-k]]
            window[s[i]]=window.get(s[i],0)+1
            if window==dicti:
                output.append(i-k+1)
        return output


