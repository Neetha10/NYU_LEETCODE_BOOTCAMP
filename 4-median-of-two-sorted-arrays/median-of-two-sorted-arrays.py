class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        output=[]
        i=0
        j=0
        while i< (len(nums1)) and j < (len(nums2)):
            if nums1[i]<= nums2[j]:
                output.append(nums1[i])
                i+=1
            else:
                output.append(nums2[j])
                j+=1
        while i<len(nums1):
            output.append(nums1[i])
            i+=1
        while j<len(nums2):
            output.append(nums2[j])
            j+=1
        n=len(output)
        mid=n//2
        if n%2==1:
            return float((output[mid]))
        else:
            return (output[mid - 1] + output[mid]) / 2.0
            



    
            