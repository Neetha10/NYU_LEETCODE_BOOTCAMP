# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap=[]
        if list1:
            heapq.heappush(heap,(list1.val,0,list1))
        if list2:
            heapq.heappush(heap,(list2.val,1,list2))
        d=ListNode()
        curr=d
        while heap:
            val,i,node=heapq.heappop(heap)
            curr.next=node
            curr=node
            node=node.next
            if node:
                heapq.heappush(heap,(node.val,i,node))
        return d.next


        