# tqo sum

class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j])==target:
                    return [i,j]

#palindrome number
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return original == reversed_num
