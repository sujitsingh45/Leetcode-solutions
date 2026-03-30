# Definition for singly-linked list.
#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head # if the list is null or omly one element just return the head
        curr=head
        while curr!=None and curr.next!=None:
            if curr.next.val==curr.val: #checking the duplicates
                curr.next=curr.next.next#deleting the duplicates                             
            else:
                curr=curr.next # if not duplicates just next
        return head             
        # time complexity o(n) iterating loop n times
        # space complexity o(1) no more data structure uses
       