# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        currVal = node.val
        nextNode = node.next
        nextNodeval = nextNode.val
        nextNode.val = currVal
        node.val = nextNodeval
        
        node.next = nextNode.next
        
        