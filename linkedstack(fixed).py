class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.last = None
        self.sz = 0

    def push(self, data):
        new_node = Node(data, self.last)
        self.last = new_node
        self.sz += 1

    def pop(self):
        if self.sz > 0:

            result = self.last.data
            self.last = self.last.next
            self.sz -= 1
            return result
        else:
            return "no elements to be deleted"
    def peek(self):
        if self.sz > 0:
            return self.last.data
        else:
            return "the list is empty"
    def size(self):
        return self.sz

s = Stack()
print(s.pop())
print(s.peek())