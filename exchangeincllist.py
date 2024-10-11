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


    def traverse(self):

        if self.head == None:
            print("List is empty")
            return

        node = self.head
        print(node.data + "->", end="")
        node = node.next

        while node != self.head:
            print(node.data, end="")
            node = node.next

    def printlist(self):
        node = self.head

        if self.head is not None:
            while(True):
                print(node.data, end="")
                node = node.next
                if node == self.head:
                    break
                    

    def exchangenodes(self):
        node = self.head

        if node == None or node.next == node:
            return node

        elif node.next.next == node:
            node = node.next
            return node

        else:
            prev = None
            current = self.head
            temp = self.head

            while current.next != node:
                prev = current
                current = current.next

            current.next = temp.next
            prev.next = temp
            temp.next = current
            self.head = current

            return self.head



if __name__ == "__main__":

    ll = Linkedlist()
    for i in range(10,15):
        ll.push(i)

    ll.traverse()



