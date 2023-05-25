class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_R_L(self, node):
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
                    
    def printforward(self):
        if not self.head:
            print(self.head)
        else:
            curr = self.head
            while curr:
                if not curr:
                    break
                print(curr.data, end=" ")
                curr = curr.next
        print()

    def printreverse(self):
        if not self.tail:
            print(self.tail)
        else:
            curr = self.tail
            while curr:
                if not curr:
                    break
                print(curr.data, end=" ")
                curr = curr.prev
        print()

fNode = Node(1)
llist = DLlist()
llist.insert_R_L(fNode)
sNode = Node(2)
llist.insert_R_L(sNode)
tNode = Node(3)
llist.insert_R_L(tNode)
llist.printforward()
print("\nPrintting in reverse order\n")
llist.printreverse()
