from ting_file_management.node import Node


class LinkedList:
    def __init__(self, value=None) -> None:
        self.__length = 0
        self.__head, self.__tail = None, None
        self.__curr = None

        if type(value) in (list, tuple):
            self.extend(value)
        elif value:
            self.__init_list(value)

    def __len__(self):
        return self.__length

    def __iter__(self):
        self.__curr = self.__head
        return self

    def __next__(self):
        curr = self.__curr
        if curr:
            self.__curr = self.__curr.next
            return curr.value
        raise StopIteration

    def __init_list(self, value):
        """o(1)"""
        node = Node(value)
        self.__length = 1
        self.__head = node
        self.__tail = node

    def __remove(self, node: Node):
        """o(1)"""
        node.prev.next = node.next
        node.next.prev = node.prev
        return node.value

    def __iterate_left(self, stop: int, start=0):
        """o(n)"""
        node = self.__head.next
        while start < stop:
            start += 1
            node = node.next
        return node

    def __iterate_right(self, stop: int, start=-1):
        """o(n)"""
        node = self.__tail.prev
        while start > stop:
            start -= 1
            node = node.prev
        return node

    def __iterate(self, index: int):
        """o(n)"""
        if index < -1:
            return self.__iterate_right(index, start=1)
        return self.__iterate_left(index, start=-2)

    def extend(self, list):
        """LinkedList = o(1)
        other lista = o(n)"""
        if isinstance(list, LinkedList):
            self.__tail.next = list.__head
            list.__head.prev = self.__tail
            self.__tail = list.__tail
        else:
            for value in list:
                self.add(value)

    def add(self, value):
        """o(1)"""
        if self.__tail:
            node = Node(value, prev=self.__tail)
            self.__tail.next = node
            self.__tail = node
            self.__length += 1
        else:
            self.__init_list(value)

    def add_first(self, value):
        """o(1)"""
        if self.__head:
            node = Node(value, next=self.__head)
            self.__head.prev = node
            self.__head = node
            self.__length += 1
        else:
            self.__init_list(value)

    def pop_first(self):
        """o(1)"""
        first = self.__head
        self.__head = self.__head.next
        self.__head.prev = None
        return first

    def pop_last(self):
        """o(1)"""
        last = self.__tail
        self.__tail = self.__tail.prev
        self.__tail.next = None
        return last

    def pop(self, index=0):
        """o(n)"""
        if not (index > (0 - self.__length) and index < self.__length):
            raise IndexError
        if index == -1:
            return self.pop_last()
        if index == 0:
            return self.pop_first()
        return self.__remove(self.__iterate(index))

    def get_first(self):
        """o(1)"""
        return self.__head.value

    def get_last(self):
        """o(1)"""
        return self.__tail.value
