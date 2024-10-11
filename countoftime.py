class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlinkedlist(self):
        node = self.head
        while node:
            print(str(node.data) + "->",end="")
            node = node.next
        print("NULL")

    def countofitem(self,val):
        count = 0
        pt = self.head
        while pt is not None:
            if pt.data == val:
                count += 1
            pt = pt.next
        return count


if __name__ == '__main__':

    ll = Linkedlist()
    for i in range(5,0,-1):
        ll.push(i)

    print("count of given item is",ll.countofitem(2))

