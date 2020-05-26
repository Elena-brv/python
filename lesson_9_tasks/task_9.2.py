class Stack:

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        self.list.pop()

    def peek(self):
        if len(self.list) > 0:
            print(self.list[-1])

stack = Stack()

stack.push(2)
stack.push(3)
stack.push(5)
print(stack.list)

stack.pop()
print(stack.list)

stack.peek()

