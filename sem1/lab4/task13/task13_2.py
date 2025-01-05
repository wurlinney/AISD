class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'[{self.data}] -> {self.next}'

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.max_size is not None and self.size >= self.max_size

    def enqueue(self, value):
        if self.is_full():
            print("Переполнение")
            return
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Опустошение очереди")
            return None
        dequeued = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return dequeued

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
