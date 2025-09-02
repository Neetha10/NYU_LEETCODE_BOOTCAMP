class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      hashi=set(nums)
      longest=1
      if not nums:
        return 0
      for num in hashi:
        if num-1 not in hashi:
            length=1
            current=num

            while current+1 in hashi:
                current+=1
                length+=1
            longest=max(longest,length)
      return longest
        
      



    


        
        