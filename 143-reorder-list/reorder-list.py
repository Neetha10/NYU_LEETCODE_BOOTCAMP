# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second_link=slow.next
        slow.next=None

        cur=second_link
        prev=None
        while cur is not None:
            nextNode=cur.next
            cur.next=prev
            prev=cur
            cur=nextNode
        
        first=head
        second=prev
        dummy=ListNode(0)
        current=dummy
        dummy.next=first
        while first and second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1

            first=temp1
            second=temp2
        return current.next
            
      
            
            


        
        

            

            
            

        
        """
        Do not return anything, modify head in-place instead.
        """
        