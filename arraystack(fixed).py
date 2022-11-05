class Stack:
    def __init__(self):
        self.my_list = []

    def push(self, data):
        self.my_list.append(data)

    def pop(self):
        if len(self.my_list)>0:
            return self.my_list.pop()
        else:
            return "no elements to be deleted"

    def peek(self):
        if len(self.my_list)>0:
            return self.my_list[-1]
        else:
            return "stack is empty"
    def size(self):
        return len(self.my_list)

s = Stack()
print(s.pop())
print(s.peek())