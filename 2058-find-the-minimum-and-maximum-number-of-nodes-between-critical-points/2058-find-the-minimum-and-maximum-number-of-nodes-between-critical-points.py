# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        ptr = head
        prev = ptr
        ptr = ptr.next
        i = 0
        while not ptr.next is None :

            i+=1
           
            if ptr.val > prev.val and ptr.val > ptr.next.val:
                arr.append(i)
            if ptr.val < prev.val and ptr.val < ptr.next.val:
                arr.append(i)
            prev=prev.next
            ptr=ptr.next
            
        if len(arr)<2:
            return [-1,-1]
        mi = float('inf')
        for i in range(1,len(arr)):
            mi = min(mi,arr[i]-arr[i-1])
            
        ans = [mi,arr[-1]-arr[0]]
        return ans



