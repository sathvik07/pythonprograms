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

    def printll(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")


def circular(head):
    if head == None:
        return True

    node = head.next
    i = 0

    while (node is not None) and (node is not head):
        i = i + 1
        node = node.next

        return (node == head)


if __name__ == '__main__':
    ll = Linkedlist()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    ll.head.next = second
    second.next = third
    third.next = fourth

    if (circular(ll.head)):
        print("Yes")
    else:
        print("No")

    fourth.next = ll.head

    if (circular(ll.head)):
        print("yes")
    else:
        print("No")
