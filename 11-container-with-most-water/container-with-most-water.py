class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxi=float('-inf')
        while l<r:
            length=min(height[l],height[r])
            width=r-l
            area=length*width
            maxi=max(maxi,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxi
        
        