# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            num = 0
            mul = 1
            while node:
                num+= mul*node.val
                node = node.next
                mul*=10
            return num
        val1 = helper(l1)
        val2 = helper(l2)
        
        val3 = val1+val2
        curr = ListNode(0)
        dummy = curr
        if val3 == 0:
            return ListNode(0)
        while val3>0:
            val = val3%10
            val3//=10
            dummy.next = ListNode(val)
            dummy = dummy.next
        return curr.next





            