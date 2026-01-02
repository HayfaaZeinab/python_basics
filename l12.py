#Write a function that reverses a string. The input string is given as an array of characters s.You must do this by modifying the input array in-place with O(1) extra memory.
 for i in range((len(s)/2)):
            s[i],s[-(i+1)]=s[-(i+1)],s[i]

#Given a string s, reverse only all the vowels in the string and return it.

class Solution(object):
    def reverseVowels(self, s):
        left=0
        right=len(s)-1
        l=[]
        for i in s:
            l.append(i)

        v="aeiouAEIOU"
        while left<right:
            if l[left] not in v:
                left+=1
            elif l[right] not in v:
                right-=1
            else:
                l[left],l[right]=l[right],l[left]
                left+=1
                right-=1
        
        """
        r=""
        for i in l:
            r+=i"""
             


        return "".join(l)
        

         

        
        
