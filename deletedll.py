import gc

class Node:

    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None


class Doublylinkedlist:

    def __init__(self):
        self.head = None

    def push(self, newdata):
        new_node = newdata
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


    def printdll(self, node):
        while(node is not None):
            print(node.data, end="")
            node = node.next


    def deleteindll(self, de):

        if self.head is None and de is None:
            return

        if self.head == de:
            self.head = de.next


        if de.next is not None:
            de.next.prev = de.prev

        if de.prev is not None:
            de.prev.next = de.next

        gc.collect()




