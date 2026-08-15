# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        ptr = ans
        c = 0
        
        while l1 is not None or l2 is not None or c!=0:
            s = c
            if l1:
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next
            
            a=ListNode(s%10)
            ptr.next=a
            ptr=ptr.next
            c=s//10
            
           
        
        
        return ans.next