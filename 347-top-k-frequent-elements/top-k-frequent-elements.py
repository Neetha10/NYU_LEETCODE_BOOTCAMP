class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output=[]
        count={}
        for numbers in nums:
            if numbers not in count:
                count[numbers]=1
            else:
                count[numbers]+=1
        sorted_count=sorted(count.items(),key=lambda item: item[1],reverse=True)
        for keys in sorted_count:
            output.append(keys[0])
        return output[:k]
        

        

    
        
            
        