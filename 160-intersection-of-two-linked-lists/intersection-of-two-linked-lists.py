# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1=headA
        p2=headB
        lenA=0
        lenB=0
        # solving using length 
        while p1!=None: 
            lenA+=1
            p1=p1.next
        
        while p2!=None:
            lenB+=1
            p2=p2.next
        p1=headA
        p2=headB    
        if lenA>lenB:
            for _ in range(lenA-lenB):
                p1=p1.next
        else:
            for _ in range(lenB-lenA):
                p2=p2.next
        while p1 and  p2:
            if p1==p2:
                return p1
            p1=p1.next
            p2=p2.next
        return None        

                  