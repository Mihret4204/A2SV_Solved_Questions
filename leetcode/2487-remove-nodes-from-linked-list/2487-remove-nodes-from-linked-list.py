# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack=[]
        ptr=head

        while ptr:

            while stack and stack[-1].val<ptr.val:
                stack.pop()
            stack.append(ptr)
            ptr=ptr.next
        
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        for n in stack:
            curr.next=n
            curr=curr.next
        return dummy.next
