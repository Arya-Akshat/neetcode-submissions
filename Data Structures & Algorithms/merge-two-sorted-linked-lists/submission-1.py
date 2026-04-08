# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if not curr1 and not curr2:
            return None
        if not curr1:
            return curr2
        if not curr2:
            return curr1
        if curr1 and curr1.val <= curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            if curr2:
                head = curr2
                curr2= curr2.next
        ans = head
            
        while curr1 or curr2:
            if not curr1:
                head.next = curr2
                return ans
                
            if not curr2:
                head.next = curr1
                return ans
            if curr1 and curr2:
                if curr1.val > curr2.val:
                    head.next = curr2
                    curr2 = curr2.next
                else:
                    head.next = curr1
                    curr1 = curr1.next
            head = head.next
        return ans

