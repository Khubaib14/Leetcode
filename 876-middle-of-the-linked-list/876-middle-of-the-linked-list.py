# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while head:
            length += 1
            head = head.next
        
        cnt = 0
        start_from = length//2
        
        while temp:
            if cnt == start_from:
                break
        
            cnt += 1
            temp = temp.next
        
        return temp