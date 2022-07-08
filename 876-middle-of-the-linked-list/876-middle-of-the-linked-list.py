# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            # while checks if fast is not
            # None and the next Node is 
            # also not None
            slow = slow.next
            fast = (fast.next).next
        return slow
        
        
        
    def solOne(self):
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