# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow
        if fast:
            second=slow.next

        cur=second
        prev=None
        while cur:
            nextNode=cur.next
            cur.next=prev
            prev=cur
            cur=nextNode

        first=head
        second=prev
        while second:
            if first.val==second.val:
                first=first=first.next
                second=second.next
            else:
                return False
        return True

        

        
        
        