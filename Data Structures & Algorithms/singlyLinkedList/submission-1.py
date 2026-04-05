class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.root = None

    def get(self, index: int) -> int:
        count = 0
        cur = self.root
        while cur:
            if count == index:
                return cur.val
            cur = cur.next
            count+=1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.root
        self.root = node
        

    def insertTail(self, val: int) -> None:
        if self.root == None:
            self.root = Node(val)
            return
        node = Node(val)
        curr = self.root
        while curr.next:
            curr = curr.next
        curr.next = node
        

    def remove(self, index: int) -> bool:
        count=0
        prev = None
        cur = self.root
        while cur:
            if count == index:
                if prev:
                    prev.next = cur.next
                else:
                    self.root = cur.next
                return True
            prev = cur
            cur = cur.next
            count+=1
        return False

    def getValues(self) -> List[int]:
        ans = []
        curr = self.root
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans
        
