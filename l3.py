#paranthesis
class Solution(object):
    def isValid(self, s):
        l=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                l.append(i)
            elif i==")":
                if len(l)==0:
                    return False
                if l[-1]=="(":
                    l.pop()
                else:
                    return False
            elif i=="}":
                if len(l)==0:
                    return False
                if l[-1]=="{":
                    l.pop()
                else:
                    return False
            elif i=="]":
                if len(l)==0:
                    return False
                if l[-1]=="[":
                    l.pop()
                else:
                    return False
        return len(l)==0
            

            


        """
        :type s: str
        :rtype: bool
        """


#merging linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next
    
        
        
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        


