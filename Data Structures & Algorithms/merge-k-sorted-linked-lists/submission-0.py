# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
import itertools
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ans = ListNode()
        curr = ans
        counter = itertools.count()

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, next(counter), node))
        while heap:
            val,_,node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, next(counter), node.next))
        return ans.next
