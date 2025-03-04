class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_0=0
        count_1=0
        count_2=0
        index=0
        for i in range(len(nums)):
            if nums[i]== 0:
                count_0+=1
            elif nums[i]==1:
                count_1+=1
            elif nums[i]==2:
                count_2+=1
        for i in range(count_0):
            nums[index]=0
            index+=1
        for i in range(count_1):
            nums[index]=1
            index+=1
        for i in range(count_2):
            nums[index]=2
            index+=1
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        