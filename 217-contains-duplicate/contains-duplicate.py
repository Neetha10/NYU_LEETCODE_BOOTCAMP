class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for i in range(len(nums)):
            if nums[i] in count:
                return True
            count[nums[i]]=nums[i]
        return False
            


        

        