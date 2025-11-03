# add binary
class Solution(object):
    def addBinary(self, a, b):
        i=len(a)-1
        j=len(b)-1
        out=""
        carry=0
    
        while i>=0 or j>=0 or carry:
            x=int(a[i]) if i>=0 else 0
            y=int(b[j]) if j>=0 else 0

            s=x+y+carry

            out+=str(s%2)
            carry=s//2

            i-=1
            j-=1
#sqrt
    i=0
        while i*i<=x:
            i+=1
    
        return i-1
