from ting_file_management.abstract_queue import AbstractQueue
import collections


class Queue(AbstractQueue):
    def __init__(self):
        self.data = collections.deque()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        value = list(self.data)[0]
        self.data.popleft()
        return value

    def search(self, index):
        data = list(self.data)
        if index is None or (index >= len(data) or index <= (0 - len(data))):
            raise IndexError("Índice Inválido ou Inexistente")
        return data[index]
