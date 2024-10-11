from sys import maxsize


def createstack():
    stack = []
    return stack


def isempty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(item, " pushed to stack ")


def pop(stack):
    if isempty(stack):
        return str(-maxsize - 1)
    return stack.pop()


def peek(stack):
    if isempty(stack):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]


st = createstack()
push(st, 1)
push(st, 2)
push(st, 3)
push(st, 4)
push(st, 5)

print("peek of the stack", peek(st))
