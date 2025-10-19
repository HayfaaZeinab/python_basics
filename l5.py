# find the firrst occurence of a string in another string

class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

# Search Insert Position 
class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)

        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
 
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
