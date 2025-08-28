from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        heap=[]
        for numbers in nums:
            if numbers not in count:
                count[numbers]=1
            else:
                count[numbers]+=1
        for num , freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[]
        for freq,num in heap:
            result.append(num)
        return result
        
        

        

    
        
            
        