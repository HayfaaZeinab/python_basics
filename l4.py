#remove Dupliicates From Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        # Edge case: empty array
        if len(nums) == 0:
            return 0
    
   
        i = 0
    
   
        for j in range(1, len(nums)):
        
            if nums[j] != nums[i]:
                i += 1              
                nums[i] = nums[j]  
        return i + 1
        """
        :type nums: List[int]
        :rtype: int
        """

#Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k=k+1
        return k
