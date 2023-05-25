class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
    
    def addAtHead(self, val: int) -> None: 
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if not self.head:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(self.length - 1):
                curr = curr.next
            curr.next = node
            self.tail = node
            self.length += 1
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            node = ListNode(val)
            curr = self.head
            for _ in range(index -1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head 
            for _ in range(index -1):
                curr = curr.next
            curr.next = curr.next.next
            if index == self.length-1:
                self.tail = curr.next
        self.length -= 1

        
obj = MyLinkedList()
param_1 = obj.get(index)
obj.addAtHead(val)
obj.addAtTail(val)
obj.addAtIndex(index,val)
obj.deleteAtIndex(index)
