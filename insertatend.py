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
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")

    def insertafter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must be in linkedlist")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertatend(self, new_data):

        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def lengthoflist(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def reversellist(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def deleteatgivenposition(self, position):
        if self.head is None:
            return 0

        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("Index is out of range")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next


    def deletelist(self,):
        current = self.head

        while current:
            next_to_current = current.next
            del current.data

            current = next_to_current


    def getNthnode(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next


        assert 0
        return 0


    def getNthfromLast(self, index):
        current = self.head
        count = 0

        while current is not None:
            current = current.next
            count += 1


        if index > count:
            print("location is greater than the length of linked list")
            return

        current = self.head
        for i in range(0, count-1):
            current = current.next
        print(current.data)









if __name__ == "__main__":

    ll = Linkedlist()
    for i in range(5, 15, 1):
        ll.push(i)

    ll.printlist()
    ll.insertafter(ll.head, 6)
    print("after inserting")
    ll.printlist()
    print("list after inserting at end",ll.insertatend(4))
    ll.printlist()
    print("length of list",ll.lengthoflist())
    print("reversed list")
    ll.reversellist()
    ll.printlist()
    ll.deleteatgivenposition(2)
    print("after deleting at given position")
    ll.printlist()
    # ll.deleteNode(ll.head, 5)
    # print("after deleting at deleting node")
    # ll.printlist()
    # ll.deletelist()
    # print("after deleting list")
    # ll.printlist()
    print(ll.getNthnode(4))
    print(ll.getNthfromLast(3))



    # def deleteNode(head, val):
    #     if head == None:
    #         print(" element not present in the list")
    #         return -1
    #
    #     if head.data == val:
    #
    #         if head.next:
    #             head.data = head.next.data
    #             head.next = head.next.next
    #             return 1
    #         else:
    #             return 0
    #
    #     if deleteNode(head.next, val) == 0:
    #         head.next = None
    #         return 1


