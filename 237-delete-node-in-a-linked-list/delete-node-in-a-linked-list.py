# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        

        
        node.val=node.next.val  #taking one ahead value for nod which is supposed to deleted 
        node.next=node.next.next# after taking deleting that value
        