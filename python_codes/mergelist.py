class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    
    def push(self,newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    
    def PrintList(self):
        temp = self.head
        while temp:
            print (temp.data ,end = "->")
            temp = temp.next


def MergetwoLists(headA , headB):

        temp = Node(0)

        if headA is None:
            return headB

        if headB is None:
            return headA

        if headA.data <= headB.data:
            temp = headA

            temp.next = MergetwoLists(headA.next ,headB)

        else:

            temp = headB

            temp.next = MergetwoLists(headA , headB.next)


        return temp


if __name__ == "__main__":

    list1 = LinkedList()
    list1.push(1)
    list1.push(2)
    list1.push(4)


    list2 = LinkedList()
    list2.push(1)
    list2.push(3)
    list2.push(4)

    list3 = LinkedList()
    list3.head = MergetwoLists(list1.head , list2.head)

    print("the merged resulted list is :",end="")
    list3.PrintList()



