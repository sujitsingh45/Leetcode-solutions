# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
    
        for i in range(n):  # move fast pointer n step ahead ,runs n time
            fast=fast.next
        if fast==None:  #if the fast is none means delete first node
            return head.next 

        while fast.next!=None: # delete nth node,runs lenth-1 time
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next  # deleting the node
        return head       

        #time complexity  o(n)+o(n)=o(n) ,o=order of growth
       # space complexity=o(1)
        