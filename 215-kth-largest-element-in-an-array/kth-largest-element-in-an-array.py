class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n=len(nums)
        new_list=[0]*n
        for i in range(n):
            minn=heapq.heappop(nums)
            new_list[i]=minn
        sorted_list=new_list[::-1]
        return sorted_list[k-1]
        
    
        