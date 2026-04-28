"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        #step 1 : add copies after them soo A->B->C becomes A->A'->B->B'->C->C'
        while curr:
            temp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = temp
            curr = curr.next.next
        #step2 : for A' ,B' assign their random with that of A, B's randoms's copies
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None 
            curr = curr.next.next
        #step3: remove org A , B 
        orig = head
        copy = head.next
        copy_head = copy

        while orig:
            orig.next = orig.next.next
            copy.next = copy.next.next if copy.next else None
            orig = orig.next
            copy = copy.next
        return copy_head


        
        


        
        
        