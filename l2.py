
#roman to integer
class Solution(object):
    def romanToInt(self, s):
        value=0
        i=0
        while i<len(s):
            if s[i]=="I":
                if i+1<len(s) and s[i+1]=="V":
                    value+=4
                    i+=2
                    continue
                elif i+1<len(s) and s[i+1]=="X":
                    value+=9
                    i+=2
                    continue
                else:
                    value+=1
            elif s[i]=="V":
                value+=5
            elif s[i]=="X":
                if i+1<len(s) and s[i+1]=="L":
                    value+=40
                    i+=2
                    continue
                elif i+1<len(s) and s[i+1]=="C":
                    value+=90
                    i+=2
                    continue
                else:
                    value+=10
            elif s[i]=="L":
                value+=50
            elif s[i]=="C":
                if i+1<len(s) and s[i+1]=="D":
                    value+=400
                    i+=2
                    continue
                elif i+1<len(s) and s[i+1]=="M":
                    value+=900
                    i+=2
                    continue
                else:
                    value+=100
            elif s[i]=="D":
                value+=500
            elif s[i]=="M":
                value+=1000
            i+=1

        return value
        

#longest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        out=""
        for i in range(len(strs[0])):
            char=strs[0][i]
            for s in strs[1:]:
                if i>=len(s) or s[i]!=char:
                    return strs[0][:i]
        return strs[0]

                



