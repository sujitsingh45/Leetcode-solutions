# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
      def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow= head
        fast=head
        
        prev=None
        while fast!=None and fast.next!=None: # getting access at half in the list
            fast=fast.next.next
            slow=slow.next 
        if fast is not None:   # odd number of nodes
            slow = slow.next       
        
        while slow!=None:  # reversing the half of the linkesd list
            new_node=slow.next
            slow.next=prev
            prev=slow
            slow=new_node
        first=head
        second=prev
        while second:  # comparing the both list
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True        
            # time complexity =o(n)+o(n)=o(n)
            # space complexity=o(1)