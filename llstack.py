class Node:
    def __init__(self, data):
        self.data = data
        self.next  = None


class Stack:

    def __init__(self):
        self.root = None

    def isempty(self):
        return True if self.root is None else False

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.root
        self.root = new_node
        print("{} is pushed to the stack".format(new_data))


    def pop(self):
        if self.isempty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isempty():
            return float("-inf")
        return self.root.data


stack = Stack()

for i in range(1,6):
    stack.push(i)

print("peek item is -", stack.peek())
print("popped item is", stack.pop())

