class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        node = self.head

        while node:
            print(str(node.data) + "->" , end='')
            node = node.next
        print("Null")


    def printclist(self):
        node = self.head

        if node != None:

            while True:
                print(str(node.data) + "->", end='')
                node = node.next
                if node == self.head:
                    break

    def countnodes(self,head):

        current = head
        count = 0

        if (current != None):
            while True:
                current = current.next
                count += 1
                if (current == head):
                    break
        return count

    def convertslltocll(self,head):
        current = head

        while head.next is not None:
                head = head.next

        head.next  = current
        return current


if __name__ == "__main__":
    ll = Linkedlist()

    for i in range(10, 15):
        ll.push(i)
    ll.printList()
    ll.convertslltocll(ll.head)

    ll.printclist()

