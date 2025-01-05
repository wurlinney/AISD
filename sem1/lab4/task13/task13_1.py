class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'[{self.data}] -> {self.next}'

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.is_empty():
            return None
        poped = self.head.data
        self.head = self.head.next
        return poped

    def is_empty(self):
        return self.head is None

