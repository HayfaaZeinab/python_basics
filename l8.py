#climbing stairs
class Solution(object):
    def climbStairs(self, n):
        
        if n<=2:
            return n

        a,b=1,2   
        for _ in range(3,n+1):
            a,b=b,a+b

        return b

  #remove duplicate from sorted list

class Solution(object):
    def deleteDuplicates(self, head):
        current=head
        while current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next
        return head
