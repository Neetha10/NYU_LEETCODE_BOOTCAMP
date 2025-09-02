class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            left=i+1
            right=n-1
            complement=target-numbers[i]
            while left<=right:
                mid=(left+right)//2
                if numbers[mid]==complement:
                    return [i+1,mid+1]
                elif numbers[mid] >complement:
                    right=mid-1
                else:
                    left=mid+1

                
                


        


        