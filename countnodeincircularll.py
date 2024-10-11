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

    def printlist(self):
        node = self.head

        while node:
            print(str(node.data) + "->", end='')
            node = node.next
        print("Null")

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



if __name__ == "__main__":
    ll = Linkedlist()

    ll.head = Node(2)
    second = Node(3)
    third = Node(4)
    fourth = Node(5)

    ll.head.next = second
    second.next = third
    third.next = fourth

    fourth.next = ll.head

    print(ll.countnodes(ll.head))




