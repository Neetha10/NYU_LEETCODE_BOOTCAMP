class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n=len(nums)
            prefix_arr= [1] * n
            prefix=1
            for i in range(n):
                prefix_arr[i]=prefix
                prefix*=nums[i]
            
        
            suffix_arr=[1] *n
            suffix=1
            for i in range(n-1,-1,-1):
                suffix_arr[i]=suffix
                suffix*=nums[i]
        
            output_arr=[1] *n
            for i in range(n):
                output_arr[i]=prefix_arr[i] * suffix_arr[i]
            return output_arr
        
                
                
        