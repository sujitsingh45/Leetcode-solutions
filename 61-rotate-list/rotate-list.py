# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        last=head
        l=1 # length start with one bcz already we are at head
        while last.next!=None:
            last=last.next
            l=l+1
        
        #finding new tail
        k=k % l
        if k==0:
            return head
        new_tail=head
        for i in range(l-k-1):
            new_tail=new_tail.next
        last.next=head
        head=new_tail.next
        new_tail.next=None

        return head
     # time complexity  traverse to find length 0(n)+ traverse to find new tail 0(n)=0(n)
     # space complexity 0(1)


        