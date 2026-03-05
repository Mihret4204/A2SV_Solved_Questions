# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans=ListNode(0)
        ans.next=head 
        curr=ans
        
        while curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
                continue
            curr=curr.next
        return ans.next
            