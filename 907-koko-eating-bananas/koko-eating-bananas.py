class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left < right:
            mid=(left+right)//2
            k=0
            for pile in piles:
                k+=math.ceil(pile/mid) 
                if k>h:
                    break
            if k<=h:
                right=mid
            else:
                left=mid+1
        return right
    
            



        

        