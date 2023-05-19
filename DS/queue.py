class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if not self.head or not self.head.next:
            self.head = None
        else:
            curr = self.head
            while curr:
                if not curr.next.next:
                    curr.next = None
                    self.tail = curr
                    break
                curr = curr.next

    def printq(self):
        if self.head:
            curr = self.head
            while curr:
                if not curr:
                    break
                print(curr.data, end = " ")
                curr = curr.next
        print("\n-")


q = Queue()
q.push(1)
q.push(2)
q.printq()
q.pop()
q.push(3)
q.push("A")
q.push(4)
q.push(5)
q.pop()
q.printq()