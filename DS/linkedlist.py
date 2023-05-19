class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self, newNode):
        if not self.head:
            self.head = newNode
        else:
            currentnode = self.head
            while currentnode:
                if not currentnode.next:
                    break
                currentnode = currentnode.next
            currentnode.next = newNode

    def printlist(self):
        if not self.head:
            print("List is empty.")
        else:
            current = self.head
            while current.next:
                if not current:
                    break
                print(current.data)
                current = current.next

fNode = Node("1.Accept everything just the way it is")
llist = linkedlist()
llist.insert(fNode)
sNode = Node("2.Do not seek pleasure for its own sake")
llist.insert(sNode)
tNode = Node("3.Do not, under any circumstances, depend on a partial feeling")
llist.insert(tNode)
llist.printlist()