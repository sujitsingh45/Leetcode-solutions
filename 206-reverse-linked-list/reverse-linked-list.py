# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr!=None:
            new_node=curr.next  # storing next node
            curr.next=prev # reversing the node 
            prev=curr # move previous forward 
            curr=new_node# move curr forward
        return prev  #new reverse linked list

        # time complexity o(n)
        # space complexity o(1)