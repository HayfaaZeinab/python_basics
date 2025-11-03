# merge sorted arrat

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
      
        nums1[m:]=nums2
        nums1.sort()
#valid palindrome
class Solution(object):
    def isPalindrome(self, s):

        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]
