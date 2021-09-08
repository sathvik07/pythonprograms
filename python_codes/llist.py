class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode


    def deleteNode(self, position):
        
        if self.head == Node:
          return

        temp = self.head

        if position == 0:
            self.head= temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next


        temp.next = None

        temp.next = next


    def printList(self):
            temp = self.head
            while(temp):
                print (" %d " %(temp.data))
                temp = temp.next

    
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)


print ("Created linked list : " )
llist.printList()
llist.deleteNode(4)
print ("\nlinked list after deletion at postion 4 :")
llist.printList()






         
