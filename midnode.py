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

    def printlist(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")

    def printMiddle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("the middle element is", slow.data)




if __name__ == '__main__':

    ll = Linkedlist()
    for i in range(6,0,-1):
        ll.push(i)
        ll.printlist()
        ll.printMiddle()
