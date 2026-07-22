# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curSlow = head
        curFast = head

        while curFast and curFast.next:
            curSlow = curSlow.next
            curFast = curFast.next.next
            if curSlow == curFast:
                return True

        return False
        